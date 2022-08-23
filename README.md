# EMB3RS OFFLINE Lite 

Offline Standalone version of the EMB3RS platform. 

Main Features:
  - District Heating Network simulation 
  - Pinch Analysis (Internal Heat Recovery)
  - ORC design (Internal Heat Recovery)

### Input: 

Each feature need a specfic CSV, which can be obtained in the folder csv_inputs

### Output:

Currently, each simulation generates HTML reports that the user can analyze

DHN simulation reports:
  - GIS  
  - TEO
  - MM 
  - BM 
  
Pinch Analysis reports:
  - CF report
  - BM report

ORC design reports:
  - CF report
  - BM report


---

## Usage DHN Simulation

```
Terminal

clone the repo
conda env -f create environment_all.yml
conda activate new_embers_offline_v_2
git submodule update --init --recursive
git submodule update --recursive --remote

```


Simulation example code:

```python

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
platform = Embers()
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

```
As simple as that.



---
