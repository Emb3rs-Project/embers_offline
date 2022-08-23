
from Embers import Embers

#############################################################################################
#############################################################################################
# USER INTERACTION -> Create a folder inside "test" folder with your input data
# Automatically in that created folder, the reports and json files will be put there after each simulation

##################### DHN SIMULATION EXAMPLE 1 ####################
# Get file
dhn_file_path = 'test/DHN/dhn_data.xlsx'

## Run platform features - As simple as that
platform = Embers()
platform.run_dhn(file_path=dhn_file_path)

##################### DHN SIMULATION EXAMPLE 2 ####################
# Starting from an intermediate step? read the json files of the modules, to start from where you desire
# -> check below,the parameter:modules_data_json
cf_module_json = 'test/DHN/intermediate_json_files/cf.json'

## Run platform features - As simple as that
platform.run_dhn(file_path=dhn_file_path,
                 get_intermediate_steps_json=True,  # OPTIONAL
                 not_to_run_modules=['mm', 'bm'],  # OPTIONAL
                 modules_data_json={"cf": cf_module_json}
                 )  # OPTIONAL

##################### ORC SIMULATION EXAMPLE ####################
orc_file_path = 'test/ORC/orc_data.xlsx'
platform.run_design_orc(orc_file_path)

##################### PINCH SIMULATION EXAMPLE ####################
pinch_file_path = 'test/PINCH/pinch_data.xlsx'
platform.run_pinch_analysis(pinch_file_path)
