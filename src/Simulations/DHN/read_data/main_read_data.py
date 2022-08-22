import pandas as pd
from .read_data_cf import ReadDataCF
from .read_data_gis import ReadDataGIS
from .read_data_mm import ReadDataMM
from .read_data_teo import ReadDataTEO
from .read_data_bm import ReadDataBM

import copy

def main_read_data(file,not_to_run_modules):

    # NOTE: WE NEED EXCEL ERROR HANDLING!
    df_file = pd.read_excel(file, sheet_name=None)

    if "cf" in not_to_run_modules:
        cf_data = []
    else:
        cf_inputs_reader = ReadDataCF()
        cf_data = cf_inputs_reader.get_data(copy.deepcopy(df_file))

    if "gis" in not_to_run_modules:
        gis_data = []
    else:
        gis_inputs_reader = ReadDataGIS()
        gis_data = gis_inputs_reader.get_data(copy.deepcopy(df_file))

    if "teo" in not_to_run_modules:
        teo_data = []
    else:
        teo_inputs_reader = ReadDataTEO()
        teo_data = teo_inputs_reader.get_data(copy.deepcopy(df_file))

    if "mm" in not_to_run_modules:
        mm_data = []
    else:
        mm_inputs_reader = ReadDataMM()
        mm_data = mm_inputs_reader.get_data(df_file)

    if "bm" in not_to_run_modules:
        bm_data = []
    else:
        bm_inputs_reader = ReadDataBM()
        bm_data = bm_inputs_reader.get_data(copy.deepcopy(df_file))



    return cf_data, gis_data, teo_data, mm_data, bm_data