import pandas as pd

def get_fuels_data(df_sheet):

    df_sheet.rename(columns=df_sheet.iloc[0], inplace=True)
    df_sheet = df_sheet.iloc[3:]
    df_sheet = df_sheet.set_index('fuel')
    df_sheet.index.name = None
    df_sheet = df_sheet.transpose()

    return df_sheet.to_dict()


def get_simple_sources_data(df_general_data,df_streams,fuels_data):

    sources_data = []
    source = {}
    general_sources_data = {}

    df_general_data['location'] = [df_general_data['latitude'],df_general_data['longitude']]
    df_general_data['location'] = fuels_data
    df_general_data = df_general_data.transpose()

    general_data = df_general_data.to_dict()
    new_dict ={}
    for source in general_data:
        new_dict[str(source['id'])] = source

    new_dict

    for id in new_dict:
        source["raw_streams"].append(df_streams[df_streams["source_id"] == ].to_dict())

            sources_data.append(source)
            source = {}



def read_data_cf(df_file_excel):

    file = pd.read_excel('../test/inputs_test.xlsx',sheet_name=None )

    keys = ['CF - Fuels Data',
            'CF - Sources General Data',
            "CF - Simple Sources' Streams",
            'CF - Grid Connection Point',
            'CF - Sinks General Data',
            "CF - Simple Sinks' Streams",
            'CF - Sinks Buildings',
            'CF - Sinks Greenhouse',
           ]


    fuels_data = get_fuels_data(file['CF - Fuels Data'])
    simple_sources_data = get_simple_sources_data(file['CF - Sources General Data'],file["CF - Simple Sources' Streams"])
    # simple_sinks_data = get_simple_sinks_data(file['CF - Fuels Data'])
    # building_data = get_building_data(file['CF - Fuels Data'])
    # greenhouse_data = get_greenhouse_data(file['CF - Fuels Data'])


    cf_data = {}
    cf_data['fuels_data'] = fuels_data



    return cf_data