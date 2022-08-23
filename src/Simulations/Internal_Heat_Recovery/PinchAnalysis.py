from cf_module.src.Source.simulation.Heat_Recovery.convert_pinch_isolated_streams import convert_pinch_isolated_streams
from cf_module.src.utilities.kb import KB
from cf_module.src.utilities.kb_data import kb
from cf_module.standalone.read_data.read_data_cf_pinch import ReadDataCFPinch
from cf_module.src.utilities.fuel_data_fill_values import fuel_data_fill_values
import pandas as pd
from cf_module.standalone.mappings.mapping_pinch_analysis import mapping_pinch_analysis
import os
import json

class PinchAnalysis:

    def __init__(self, output_folder, json_folder):
        self.output_folder = output_folder
        self.json_folder = json_folder
        self.sources = []

    def read_user_inputs(self, file):
        df_file = pd.read_excel(file, sheet_name=None)
        cf_pinch = ReadDataCFPinch()
        self.cf_data = cf_pinch.get_data(df_file)

        # fuels_data
        self.cf_data["fuels_data"] = fuel_data_fill_values(self.cf_data["sources"][0]['location'],
                                                           self.cf_data["fuels_data"],
                                                           KB(kb))

    def simulation(self):
        in_var = mapping_pinch_analysis(self.cf_data)
        self.pinch_data = convert_pinch_isolated_streams(in_var, KB(kb))


    def get_report(self):
        file = open(os.path.join(self.output_folder, "pinch_results.html"), "w")
        file.write(self.pinch_data["report"])
        file.close()


    def get_json(self):
        full_path = os.path.join(self.json_folder, "pinch_results.json")
        with open(full_path, "w") as outfile:
            outfile.write(json.dumps(self.pinch_data))