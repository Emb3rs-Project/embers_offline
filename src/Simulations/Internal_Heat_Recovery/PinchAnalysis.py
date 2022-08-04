from cf_module.src.Source.simulation.Heat_Recovery.convert_pinch_isolated_streams import convert_pinch_isolated_streams
from cf_module.src.utilities.kb import KB
from cf_module.src.utilities.kb_data import kb
from src.Simulations.Internal_Heat_Recovery.mappings.mapping_pinch_isolated_streams import mapping_pinch_isolated_streams
from src.Simulations.Internal_Heat_Recovery.read_data.read_pinch import ReadDataPinchIsolatedStreams
from cf_module.src.utilities.fuel_data_fill_values import fuel_data_fill_values
import os

class PinchAnalysis:

    def read_user_inputs(self, file):
        cf_inputs = ReadDataPinchIsolatedStreams()
        self.cf_data_raw = cf_inputs.get_data(file)
        self.fill_fuels_data()


    def fill_fuels_data(self):
        # fuels_data
        self.fuels_data = fuel_data_fill_values(self.cf_data_raw['location'],
                                                self.cf_data_raw["fuels_data"],
                                                KB(kb))

        self.cf_data_raw["fuels_data"] = self.fuels_data

    def run_simulation(self):

        pinch_analysis_input = mapping_pinch_isolated_streams(self.cf_data_raw)
        self.pinch_analysis_results = convert_pinch_isolated_streams(pinch_analysis_input, KB(kb))

    def get_reports(self, output_folder):
        file = open(os.path.join(output_folder, "pinch_analysis_results.html"), "w")
        file.write(self.pinch_analysis_results["report"])
        file.close()


    def get_parameters_values(self, key, val):
        import ast
        new_val = {
            "saturday_on": {"yes": 1, "no": 0},
            "sunday_on": {"yes": 1, "no": 0},
            "space_heating_type": {"Conventional": 1, "Low temperature": 2},
            "building_orientation": {
                                    "North": "N",
                                    "South": "S",
                                    "East": "E",
                                    "West": "W"},
        }

        if key == "real_hourly_capacity" or key == "real_monthly_capacity":
            val = ast.literal_eval(val)
            return val

        elif key in new_val:
            return new_val[key][val]
        else:
            return val
