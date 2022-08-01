from cf_module.src.utilities.fuel_data_fill_values import fuel_data_fill_values
from cf_module.src.Source.simulation.Convert.convert_sources import convert_sources
from cf_module.src.Sink.simulation.convert_sinks import convert_sinks
from cf_module.src.Sink.characterization.building import building
from cf_module.src.Sink.characterization.greenhouse import greenhouse
from cf_module.src.General.Simple_User.simple_user import simple_user
from cf_module.src.utilities.kb import KB
from cf_module.src.utilities.kb_data import kb
from src.mappings.cf.mapping_convert_sinks import mapping_convert_sinks
from src.mappings.cf.mapping_convert_sources import mapping_convert_sources
from src.mappings.cf.mapping_building import mapping_building
from src.mappings.cf.mapping_greenhouse import mapping_greenhouse
from src.mappings.cf.mapping_simple_user import mapping_simple_user
from gis_module.functions.create_network import run_create_network
from gis_module.functions.optimize_network import run_optimize_network
from gis_module.utilities import kb_data as gis_kb
from src.mappings.teo.mapping_teo import mapping_teo
from src.read_data.main_read_data import main_read_data
from src.mappings.gis.mapping_create_network import mapping_create_network
from src.mappings.gis.mapping_optimize_network import mapping_optimize_network
from teo_module.module.src.integration import run_build_model

class Embers:

    def run_dhn(self, file):
        dhn = self.DHNAssessment()
        dhn.read_user_inputs(file)
        dhn.run_simulation()

    #def run_pinch_analysis(self, file):
    #    pinch = self.PinchAnalysis()
#
    #def run_design_orc(self, file):
    #    orc = self.DesignORC()

    #class PinchAnalysis:
#
    #class DesignORC:

    class DHNAssessment:

        def __init__(self):
            self.sources = []
            self.sinks = []

        def read_user_inputs(self, file):
            cf_data_raw, self.gis_data, self.teo_data = main_read_data(file)

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

            self.cf_simulation()
            self.gis_simulation()
            self.teo_simulation()

            iteration = True
            import json
            ex_cap_json = json.load(open("test/Ex_cap_itr1.json"))

           # while iteration == True:
           #     self.teo_simulation()
#
           #     if a == 1:
           #         iteration = False
           #     else:
           #         self.gis_simulation(ex_cap_json)

            # teo

            # if "mm_bm" not in not_to_run_modules:
            # mm

            # bm

            print("DHN Simulation - COMPLETED!")

        def cf_simulation(self):
            print("CF STARTED!")
            convert_sinks_input = mapping_convert_sinks(self.sinks)
            self.convert_sinks_data = convert_sinks(convert_sinks_input, KB(kb))

            convert_sources_input = mapping_convert_sources(self.sources)
            self.convert_sources_data = convert_sources(convert_sources_input, KB(kb))
            print("CF COMPLETED!")

        def gis_simulation(self, teo_data={"ex_cap": []}):
            print("GIS STARTED!")

            import warnings
            warnings.filterwarnings("ignore")

            create_network_input = mapping_create_network(self.gis_data,
                                                          self.convert_sinks_data,
                                                          self.convert_sources_data,
                                                          teo_data
                                                          )

            self.create_network_data = run_create_network(create_network_input, gis_kb.kb)

            optimize_network_input = mapping_optimize_network(self.gis_data,
                                                              self.create_network_data,
                                                              self.convert_sources_data,
                                                              self.convert_sinks_data)

            self.optimize_network_data = run_optimize_network(optimize_network_input, gis_kb.kb)

            print("GIS COMPLETED!")

        def teo_simulation(self):

            teo_input = mapping_teo(self.optimize_network_data,
                                    self.convert_sinks_data,
                                    self.convert_sources_data,
                                    self.teo_data)

            import json
            with open("teo_data.json", "w") as outfile:
                json.dump(teo_input, outfile)

            self.teo_run_model_data = run_build_model(teo_input)
           




            a = 1

    # def pinch_analysis(self):
    #    # cf
    #    best_options, cf_report = convert_pinch_isolated_streams()


#
#    # bm
#
#
# def design_orc(self):
#    # cf
#    best_options, cf_report = convert_orc()
#
#    # bm


####################################################################################

# get file
excel_file = 'test/inputs_test.xlsx'

# platform
platform = Embers()
platform.run_dhn(excel_file)
# platform.pinch_analysis()
# platform.design_orc()
