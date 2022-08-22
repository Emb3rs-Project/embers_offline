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

Simulation example code:

```python
from Embers import Embers

platform_offline = Embers()

# Get file
dhn_file_path = 'test/DHN/dhn_data.xlsx'
platform_offline.run_dhn(file_path=dhn_file_path)

# It always creates a folder ("intermediate_json_files") with json files of each module, and an output folder ("output") with the reports of each module

```
As simple as that.

Extra features:
```python
from Embers import Embers

dhn_file_path = 'test/DHN/dhn_data.xlsx'

# Starting from an intermediate step? read the json files of the modules, to start from where you desire
# -> check below,the parameter:modules_data_json
cf_module_json = 'test/DHN/intermediate_json_files/cf.json'

## Run platform features - As simple as that
platform = Embers()
platform.run_dhn(file_path=dhn_file_path,
                 get_intermediate_steps_json=True,  # OPTIONAL
                 not_to_run_modules=['mm', 'bm'],  # OPTIONAL
                 modules_data_json={"cf": cf_module_json})  # OPTIONAL

```


---
