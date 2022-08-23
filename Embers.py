import json
import os
from src.Simulations.DHN.DHNAssessment import DHNAssessment
from src.Simulations.Internal_Heat_Recovery.DesignORC import DesignORC
from src.Simulations.Internal_Heat_Recovery.PinchAnalysis import PinchAnalysis

# Main
class Embers:

    def run_dhn(self, file_path, not_to_run_modules=None, modules_data_json=None, get_intermediate_steps_json=True):

        dhn_excel_file = os.path.abspath(file_path)
        dir_path = os.path.dirname(dhn_excel_file)

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

    # TODO: NOT YET FINISHED
    #def run_design_orc(self, orc_file, output_folder):
    #    orc = DesignORC()
    #    orc.read_user_inputs(orc_file)
    #    orc.run_simulation()
    #    orc.get_reports(output_folder)

    #def run_pinch_analysis(self, pinch_file,output_folder):
    #    pinch = PinchAnalysis()
    #    pinch.read_user_inputs(pinch_file)
    #    pinch.run_simulation()
    #    pinch.get_reports(output_folder)
#
#############################################################################################
#############################################################################################
# USER INTERACTION -> Users have to put the correct file name to be read on the "test" folder.

# DHN SIMULATION EXAMPLE ####################
# Get file
dhn_file_path = 'test/DHN/dhn_data.xlsx'

# Starting from an intermediate step? read the json files of the modules, to start from where you desire
# -> check below,the parameter:modules_data_json
cf_module_json = 'test/DHN/intermediate_json_files/cf.json'

## Run platform features - As simple as that
platform = Embers()
platform.run_dhn(file_path=dhn_file_path,
                 get_intermediate_steps_json=False,  # OPTIONAL
                 not_to_run_modules=['mm', 'bm'],  # OPTIONAL
                 modules_data_json={"cf": cf_module_json})  # OPTIONAL


#orc_excel_file = os.path.abspath('test/inputs/orc_data.xlsx')
#pinch_excel_file = os.path.abspath('test/inputs/pinch_data.xlsx')

#platform.run_pinch_analysis(pinch_excel_file, output_folder)
#platform.run_design_orc(pinch_excel_file, output_folder)


