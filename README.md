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

DHN simulation:
  - GIS
  - TEO
  - MM
  - BM
  
Pinch Analysis:
  - CF
  - BM

ORC design:
  - CF
  - BM


---

## Usage

Simulation example code:

```python
from Embers import Embers

platform_offline = Embers()
platform_offline.run_dhn("csv_inputs/dhn.csv")
platform_offline.run_pinch_analysis("csv_inputs/pinch_analysis.csv")
platform_offline.run_design_orc("csv_inputs/design_orc.csv")

```
As simple as that.


---
