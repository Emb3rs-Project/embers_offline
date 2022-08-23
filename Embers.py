import json
import os
from src.Simulations.DHN.DHNAssessment import DHNAssessment
from src.Simulations.Internal_Heat_Recovery.DesignORC import DesignORC
from src.Simulations.Internal_Heat_Recovery.PinchAnalysis import PinchAnalysis


# Main
class Embers:

    def folder_creator(self, file):
        dir_path = os.path.dirname(file)

        # Save outputs in this folder
        if os.path.exists(os.path.join(dir_path, 'output')) == False:
            output_folder_path = os.path.join(dir_path, 'output')
            os.mkdir(output_folder_path)
        else:
            output_folder_path = os.path.join(dir_path, 'output')

        if os.path.exists(os.path.join(dir_path, 'intermediate_json_files')) == False:
            json_files_folder_path = os.path.join(dir_path, 'intermediate_json_files')
            os.mkdir(json_files_folder_path)
        else:
            json_files_folder_path = os.path.join(dir_path, 'intermediate_json_files')

        output_folder = os.path.abspath(output_folder_path)
        json_folder = os.path.abspath(json_files_folder_path)

        return output_folder, json_folder

    def run_dhn(self, file_path, not_to_run_modules=None, modules_data_json=None, get_intermediate_steps_json=True):

        dhn_excel_file = os.path.abspath(file_path)
        output_folder, json_folder = self.folder_creator(dhn_excel_file)

        # Check user inputs
        if not_to_run_modules == None:
            not_to_run_modules = []

        if modules_data_json != None:
            for module in modules_data_json.keys():
                modules_data_json[module] = json.load(open(modules_data_json[module]))
                if module not in not_to_run_modules:
                    not_to_run_modules.append(module)
        else:
            modules_data_json = {}

        modules_data_json.setdefault('cf')
        modules_data_json.setdefault('gis')
        modules_data_json.setdefault('teo')
        modules_data_json.setdefault('mm')

        if (modules_data_json["gis"] is None and modules_data_json["teo"] is not None) or (modules_data_json["gis"] is not None and modules_data_json["teo"] is None):
            raise Exception("Introduce GIS and TEO json file, or none")

        # Run Simulation
        dhn = DHNAssessment(output_folder, json_folder, not_to_run_modules, get_intermediate_steps_json)
        dhn.read_user_inputs(dhn_excel_file)
        dhn.run_simulation(modules_data_json)

    def run_design_orc(self, file_path):

        orc_file = os.path.abspath(file_path)
        output_folder, json_folder = self.folder_creator(orc_file)
        platform_orc = DesignORC(output_folder, json_folder)
        platform_orc.read_user_inputs(orc_file)
        platform_orc.simulation()
        platform_orc.get_report()
        platform_orc.get_json()


    def run_pinch_analysis(self, file_path):

        pinch_file = os.path.abspath(file_path)
        output_folder, json_folder = self.folder_creator(pinch_file)
        platform_pinch_analysis = PinchAnalysis(output_folder, json_folder)
        platform_pinch_analysis.read_user_inputs(pinch_file)
        platform_pinch_analysis.simulation()
        platform_pinch_analysis.get_report()
        platform_pinch_analysis.get_json()



