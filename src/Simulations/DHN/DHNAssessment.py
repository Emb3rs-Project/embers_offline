from cf_module.src.utilities.fuel_data_fill_values import fuel_data_fill_values
from cf_module.src.Source.simulation.Convert.convert_sources import convert_sources
from cf_module.src.Sink.simulation.convert_sinks import convert_sinks
from cf_module.src.Sink.characterization.building import building
from cf_module.src.Sink.characterization.greenhouse import greenhouse
from cf_module.src.General.Simple_User.simple_user import simple_user
from cf_module.src.utilities.kb import KB
from cf_module.src.utilities.kb_data import kb
from src.Simulations.DHN.mappings.cf.mapping_convert_sinks import mapping_convert_sinks
from src.Simulations.DHN.mappings.cf.mapping_convert_sources import mapping_convert_sources
from src.Simulations.DHN.mappings.cf.mapping_building import mapping_building
from src.Simulations.DHN.mappings.cf.mapping_greenhouse import mapping_greenhouse
from src.Simulations.DHN.mappings.cf.mapping_simple_user import mapping_simple_user
from gis_module.functions.create_network import run_create_network
from gis_module.functions.optimize_network import run_optimize_network
from gis_module.utilities import kb_data as gis_kb
from src.Simulations.DHN.mappings.teo.mapping_teo import mapping_teo
from src.Simulations.DHN.read_data.main_read_data import main_read_data
from src.Simulations.DHN.mappings.gis.mapping_create_network import mapping_create_network
from src.Simulations.DHN.mappings.gis.mapping_optimize_network import mapping_optimize_network
from teo_module.module.src.integration import run_build_model
from market_module.market_module.long_term.main_longterm import main_longterm
from src.Simulations.DHN.mappings.mm.mapping_mm import mapping_mm
from src.Simulations.DHN.mappings.bm.mapping_bm_dhn import mapping_bm_dhn
from business_module.Businessmodulev1_clean import BM
import os
import json

class DHNAssessment:

    def __init__(self, output_folder, json_folder, not_to_run_modules, get_intermediate_steps_json):
        self.sources = []
        self.sinks = []
        self.not_to_run_modules = not_to_run_modules
        self.get_intermediate_steps_json = get_intermediate_steps_json
        self.output_folder = output_folder
        self.json_folder = json_folder


    def read_user_inputs(self, file):
        cf_data_raw, self.gis_data, self.teo_data, self.mm_data, self.bm_data = main_read_data(file, self.not_to_run_modules)

        if "cf" not in self.not_to_run_modules:
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
                    _sink_raw["name"] = _sink_raw["name"]
                    del _sink_raw['info']

                elif sink_type == "greenhouse":
                    _data = mapping_greenhouse(_sink_raw)
                    _char_streams = greenhouse(_data)
                    _sink_raw["name"] = _sink_raw["info"]["name"]
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

    def run_simulation(self, modules_data_json):
        print("DHN Simulation STARTED!")

        # CF
        if modules_data_json["cf"] is None:
            self.cf_simulation()

            if self.get_intermediate_steps_json == True:
                self.get_json("cf", {
                    "convert_sinks_results": self.convert_sinks_results,
                    "convert_sources_results": self.convert_sources_results})

        else:
            self.convert_sinks_results = modules_data_json["cf"]["convert_sinks_results"]
            self.convert_sources_results = modules_data_json["cf"]["convert_sources_results"]

        # GIS-TEO iteration
        if modules_data_json["gis"] is None and modules_data_json["teo"] is None:
            iteration = True
            losses_last_iteration = 1
            self.teo_results = {"ex_capacities": []}

            while iteration == True:
                self.gis_simulation(self.teo_results)

                if "teo" not in self.not_to_run_modules:
                    if abs(self.optimize_network_results["losses_cost_kw"]["losses_in_kw"] - losses_last_iteration) / losses_last_iteration * 100 < 5:  # <5% converge
                        iteration = False

                        if self.get_intermediate_steps_json == True:

                            exclude_keys = ["map_report"] # Map would be represented in a different format if converted
                            optimize_network_results_except_map_report = {k: self.optimize_network_results[k] for k in set(list(self.optimize_network_results.keys())) - set(exclude_keys)}

                            self.get_json("gis", {
                                "optimize_network_results": optimize_network_results_except_map_report})

                            self.get_json("teo", self.teo_results)

                        self.get_report("teo", self.teo_results)
                        self.get_gis_report(self.optimize_network_results)
                    else:
                        losses_last_iteration = self.optimize_network_results["losses_cost_kw"]["losses_in_kw"].copy()
                        self.teo_simulation()
                else:
                    exclude_keys = ["map_report"]  # Map would be represented in a different format if converted
                    optimize_network_results_except_map_report = {k: self.optimize_network_results[k] for k in
                                                                  set(list(self.optimize_network_results.keys())) - set(
                                                                      exclude_keys)}

                    self.get_json("gis", {
                        "optimize_network_results": optimize_network_results_except_map_report})

                    break

        else:
            self.optimize_network_results = modules_data_json["gis"]["optimize_network_results"]
            self.teo_results = modules_data_json["teo"]



        # MM
        if "mm" not in self.not_to_run_modules:
            if modules_data_json["mm"] is None:
                self.mm_simulation()
                if self.get_intermediate_steps_json == True:
                    self.get_json("mm", self.mm_results)
            else:
                self.mm_results = modules_data_json["mm"]

            self.get_report("mm", self.mm_results)

        # BM
        if "bm" not in self.not_to_run_modules:
            self.bm_simulation()

            if self.get_intermediate_steps_json == True:
                if self.get_intermediate_steps_json == True:
                    self.get_json("bm", self.bm_results)

            self.get_report("bm", self.bm_results)

        print("DHN Simulation - COMPLETED!")

    def cf_simulation(self):
        print("CF STARTED!")

        convert_sinks_input = mapping_convert_sinks(self.sinks, self.gis_data)

        self.convert_sinks_results = convert_sinks(convert_sinks_input, KB(kb))

        convert_sources_input = mapping_convert_sources(self.sources)
        self.convert_sources_results = convert_sources(convert_sources_input, KB(kb))

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
        self.get_json("gis_optimize_network_input", optimize_network_input)

        self.optimize_network_results = run_optimize_network(optimize_network_input, gis_kb.kb)

        print("GIS COMPLETED!")

    def teo_simulation(self):
        print("TEO STARTED!")

        teo_input = mapping_teo(self.optimize_network_results,
                                self.convert_sinks_results,
                                self.convert_sources_results,
                                self.teo_data)

        self.get_json("teo_input", teo_input)
        self.teo_results = run_build_model(teo_input)

        print("TEO COMPLETED!")

    def mm_simulation(self):
        print("MM STARTED!")

        mm_input = mapping_mm(self.teo_results, self.convert_sinks_results, self.mm_data)
        self.get_json("mm_input", mm_input)
        self.mm_results = main_longterm(mm_input)

        print("MM COMPLETED!")

    def bm_simulation(self):
        print("BM STARTED!")

        bm_input = mapping_bm_dhn(self.teo_results, self.mm_results, self.optimize_network_results, self.bm_data)
        self.get_json("bm_input", bm_input)
        self.bm_results = BM(bm_input)

        print("BM COMPLETED!")

    def get_report(self, module, data):

        file = open(os.path.join(self.output_folder, module + "_results.html"), "w")
        file.write(data["report"])
        file.close()

    def get_gis_report(self, data):

        file = open(os.path.join(self.output_folder, "gis_results.html"), "w")
        file.write(self.optimize_network_results["report"])
        file.write(data["report"])
        file.close()

        self.optimize_network_results["map_report"].save(os.path.join(self.output_folder, "gis_map.html"))

    def get_json(self, module, data):
        full_path = os.path.join(self.json_folder, module + ".json")
        with open(full_path, "w") as outfile:
            outfile.write(json.dumps(data))

