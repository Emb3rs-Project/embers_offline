from cf_module.src.General.Simple_User.simple_user import simple_user
from cf_module.src.Source.simulation.Heat_Recovery.ORC.convert_orc import convert_orc
import os
from cf_module.standalone.mappings.mapping_simple_user import mapping_simple_user
from cf_module.src.utilities.fuel_data_fill_values import fuel_data_fill_values
from cf_module.src.utilities.kb import KB
from cf_module.src.utilities.kb_data import kb
from cf_module.standalone.mappings.mapping_convert_orc import mapping_convert_orc
from cf_module.standalone.read_data.read_data_cf_design_orc import ReadDataCFORC
import json
import pandas as pd

class DesignORC:

    def __init__(self, output_folder, json_folder):
        self.output_folder = output_folder
        self.json_folder = json_folder
        self.sources = []

    def read_user_inputs(self, file):
        df_file = pd.read_excel(file, sheet_name=None)
        cf_orc = ReadDataCFORC()

        self.cf_data = cf_orc.get_data(df_file)
        self.characterization()

    def characterization(self):
        # fuels_data
        self.fuels_data = fuel_data_fill_values(self.cf_data["sources"][0]['location'],
                                                self.cf_data["fuels_data"],
                                                KB(kb))

        # sources
        for _source_raw in self.cf_data["sources"]:
            _data = mapping_simple_user(_source_raw, "source")
            _char_streams = simple_user(_data)

            del _source_raw['raw_streams']
            _source_raw["streams"] = _char_streams["streams"]
            self.sources.append(_source_raw)

    def simulation(self):
        in_var = mapping_convert_orc(self.fuels_data, self.sources, self.cf_data["orc_data"])
        self.convert_orc_results = convert_orc(in_var, kb)


    def get_report(self):
        file = open(os.path.join(self.output_folder, "orc_results.html"), "w")
        file.write(self.convert_orc_results["report"])
        file.close()


    def get_json(self):
        full_path = os.path.join(self.json_folder, "orc_results.json")
        with open(full_path, "w") as outfile:
            outfile.write(json.dumps(self.convert_orc_results))