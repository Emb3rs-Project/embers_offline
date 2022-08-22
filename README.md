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
dhn_file_path = 'test/DHN/dhn_data.xlsx'
platform_offline.run_dhn(file_path=dhn_file_path)

```
As simple as that.


---
