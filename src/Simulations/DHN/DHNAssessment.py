from ....cf_module.src.utilities.fuel_data_fill_values import fuel_data_fill_values
from ....cf_module.src.Source.simulation.Convert.convert_sources import convert_sources
from ....cf_module.src.Sink.simulation.convert_sinks import convert_sinks
from ....cf_module.src.Sink.characterization.building import building
from ....cf_module.src.Sink.characterization.greenhouse import greenhouse
from ....cf_module.src.General.Simple_User.simple_user import simple_user
from ....cf_module.src.utilities.kb import KB
from ....cf_module.src.utilities.kb_data import kb
from .mappings.cf.mapping_convert_sinks import mapping_convert_sinks
from .mappings.cf.mapping_convert_sources import mapping_convert_sources
from .mappings.cf.mapping_building import mapping_building
from .mappings.cf.mapping_greenhouse import mapping_greenhouse
from .mappings.cf.mapping_simple_user import mapping_simple_user
from ....gis_module.functions.create_network import run_create_network
from ....gis_module.functions.optimize_network import run_optimize_network
from ....gis_module.utilities import kb_data as gis_kb
from .mappings.teo.mapping_teo import mapping_teo
from .read_data.main_read_data import main_read_data
from .mappings.gis.mapping_create_network import mapping_create_network
from .mappings.gis.mapping_optimize_network import mapping_optimize_network
from ....teo_module.module.src.integration import run_build_model
from ....market_module.market_module.long_term.main_longterm import main_longterm
from .mappings.mm.mapping_mm import mapping_mm
from ....market_module.market_module.long_term.market_functions.convert_user_and_module_inputs import convert_user_and_module_inputs
from .mappings.bm.mapping_bm_dhn import mapping_bm_dhn
from ....business_module.Businessmodulev1_clean import BM

import json

class DHNAssessment:

    def __init__(self):
        self.sources = []
        self.sinks = []

    def read_user_inputs(self, file):
        cf_data_raw, self.gis_data, self.teo_data, self.mm_data = main_read_data(file)

        self.cf_characterization(cf_data_raw)

    def cf_characterization(self, cf_data_raw):
        print("CF Characterization STARTED!")

        # fuels_data
        self.fuels_data = fuel_data_fill_values(cf_data_raw["sources"][0]['location'],
                                                cf_data_raw["fuels_data"],
                                                KB(kb))

        # sources
        for _source_raw in cf_data_raw["sources"]:
            _data = mapping_simple_user(_source_raw, "source")
            _char_streams = simple_user(_data)

            del _source_raw['raw_streams']
            _source_raw["streams"] = _char_streams["streams"]
            _source_raw["fuels_data"] = self.fuels_data
            self.sources.append(_source_raw)

        # sinks
        for sink_type in cf_data_raw["sinks"]:
            for _sink_raw in cf_data_raw["sinks"][str(sink_type)]:
                if sink_type == "building":
                    _data = mapping_building(_sink_raw)
                    _char_streams = building(_data, KB(kb))
                    del _sink_raw['info']

                elif sink_type == "greenhouse":
                    _data = mapping_greenhouse(_sink_raw)
                    _char_streams = greenhouse(_data)
                    del _sink_raw['info']

                elif sink_type == "simple_sink":
                    _data = mapping_simple_user(_sink_raw, "sink")
                    _char_streams = simple_user(_data)
                    del _sink_raw['raw_streams']

                else:
                    raise Exception("Sink type not valid")

                _sink_raw["streams"] = _char_streams["streams"]
                _sink_raw["fuels_data"] = self.fuels_data

                self.sinks.append(_sink_raw)

        print("CF Characterization COMPLETED!")

    def run_simulation(self, not_to_run_modules=None):
        print("DHN Simulation STARTED!")

        # CF
        self.cf_simulation()
        #
        # GIS-TEO iteration start
        iteration = True
        losses_last_iteration = 1
        self.teo_results = {"ex_capacities": []}

        while iteration == True:
            self.gis_simulation(self.teo_results)
            if abs(self.optimize_network_results["losses_cost_kw"][
                       "losses_in_kw"] - losses_last_iteration) / losses_last_iteration * 100 < 5:  # <5% converge
                iteration = False
            else:
                losses_last_iteration = self.optimize_network_results["losses_cost_kw"]["losses_in_kw"].copy()
                self.teo_simulation()

        if not_to_run_modules != ["mm", "bm"]:
            # MM
            self.mm_simulation()

            # BM
            # self.bm_simulation()

        print("DHN Simulation - COMPLETED!")

    def cf_simulation(self):
        print("CF STARTED!")
        convert_sinks_input = mapping_convert_sinks(self.sinks)
        self.convert_sinks_results = convert_sinks(convert_sinks_input, KB(kb))

        convert_sources_input = mapping_convert_sources(self.sources)
        self.convert_sources_results = convert_sources(convert_sources_input, KB(kb))
        print("CF COMPLETED!")

        with open("convert_sinks_results.json", "w") as outfile:
            json.dump(self.convert_sinks_results, outfile)

        with open("convert_sources_results.json", "w") as outfile:
            json.dump(self.convert_sources_results, outfile)

    def gis_simulation(self, teo_data):
        print("GIS STARTED!")

        import warnings
        warnings.filterwarnings("ignore")

        create_network_input = mapping_create_network(self.gis_data,
                                                      self.convert_sinks_results,
                                                      self.convert_sources_results,
                                                      teo_data
                                                      )

        self.create_network_results = run_create_network(create_network_input, gis_kb.kb)

        optimize_network_input = mapping_optimize_network(self.gis_data,
                                                          self.create_network_results,
                                                          self.convert_sources_results,
                                                          self.convert_sinks_results)

        self.optimize_network_results = run_optimize_network(optimize_network_input, gis_kb.kb)

        print("GIS COMPLETED!")

        exclude_keys = ['map_report']
        data = {k: self.optimize_network_results[k] for k in set(list(self.optimize_network_results.keys())) - set(exclude_keys)}

        with open("optimize_network_results.json", "w") as outfile:
            json.dump(data, outfile)

    def teo_simulation(self):
        print("TEO STARTED!")

        teo_input = mapping_teo(self.optimize_network_results,
                                self.convert_sinks_results,
                                self.convert_sources_results,
                                self.teo_data)

        with open("teo_input.json", "w") as outfile:
            json.dump(teo_input, outfile)

        self.teo_results = run_build_model(teo_input)

        print("TEO COMPLETED!")

        with open("teo_results.json", "w") as outfile:
            json.dump(self.teo_results, outfile)

    def mm_simulation(self):
        print("MM STARTED!")

        mm_input = mapping_mm(self.teo_results, self.convert_sinks_results, self.mm_data)
        mm_input_converted = convert_user_and_module_inputs(mm_input)

        self.mm_results = main_longterm(mm_input_converted)

        print("MM COMPLETED!")

        with open("mm_results.json", "w") as outfile:
            json.dump(self.mm_results, outfile)

    def bm_simulation(self):
        print("BM STARTED!")

        bm_input = mapping_bm_dhn(self.teo_results, self.optimize_network_results, self.mm_results, self.bm_data)
        self.bm_results = BM(bm_input)

        print("BM COMPLETED!")

    def get_reports(self):

        file = open("gis_results.html", "w")
        file.write(self.optimize_network_results["report"])
        file.close()

        self.optimize_network_results["map_report"].save("gis_map.html")

        file = open("teo_results.html", "w")
        file.write(self.teo_results["report"])
        file.close()

        file = open("mm_results.html", "w")
        file.write(self.mm_results["report"])
        file.close()

        # file = open("bm_results.html", "w")
        # file.write(self.bm_results["report"])
        # file.close()
