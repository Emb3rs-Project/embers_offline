import pandas as pd
from .read_data_cf import read_data_cf

def main_read_data():

    df_file = pd.read_excel('../test/inputs_test.xlsx', sheet_name=None)

    keys = ['CF - Fuels Data',
            'CF - Sources General Data',
            "CF - Simple Sources' Streams",
            'CF - Grid Connection Point',
            'CF - Sinks General Data',
            "CF - Simple Sinks' Streams",
            'CF - Sinks Buildings',
            'CF - Sinks Greenhouse',
            'GIS',
            'MARKET',
            'TEO',
            'BM']

    cf_data = read_data_cf(df_file)
    #gis_data = read_data_gis(df_file)
    #mm_data = read_data_mm(df_file)
    #bm_data = read_data_bm(df_file)
    #mm_data = read_data_mm(df_file)

    return cf_data #,gis_data,mm_data,bm_data,mm_data