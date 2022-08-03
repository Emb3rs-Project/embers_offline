import pandas as pd
from .read_data_cf import ReadDataCF
from .read_data_gis import ReadDataGIS
from .read_data_mm import ReadDataMM
from .read_data_teo import ReadDataTEO
#from .read_data_bm import ReadDataBM

import copy

def main_read_data(file):

    # NOTE: WE NEED EXCEL ERROR HANDLING!
    df_file = pd.read_excel(file, sheet_name=None)
    cf_inputs_reader = ReadDataCF()
    cf_data = cf_inputs_reader.get_data(copy.deepcopy(df_file))
    gis_inputs_reader = ReadDataGIS()
    gis_data = gis_inputs_reader.get_data(copy.deepcopy(df_file))
    teo_inputs_reader = ReadDataTEO()
    teo_data = teo_inputs_reader.get_data(copy.deepcopy(df_file))
    #bm_inputs_reader = ReadDataBM()
    #bm_data = bm_inputs_reader.get_data(copy.deepcopy(df_file))

    mm_inputs_reader = ReadDataMM()
    mm_data = mm_inputs_reader.get_data(df_file)


    return cf_data, gis_data, teo_data, mm_data#,bm_data