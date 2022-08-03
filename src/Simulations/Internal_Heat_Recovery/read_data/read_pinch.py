import pandas as pd
import numpy as np

class ReadDataPinchIsolatedStreams:

    def get_data(self, df_file_excel):

        streams_data = df_file_excel.replace({np.nan: None})
        # convert df to dict
        streams_data = streams_data.to_dict(orient='records')

        streams_data.pop(0)  # remove units dict

        return {"streams": streams_data}


    def get_fuels_data(self, df_sheet):
        df_sheet = df_sheet.set_index('fuel')

        df_sheet["price"] = df_sheet["price"]/1000
        df_sheet.index.name = None
        df_sheet = df_sheet.transpose()
        df_sheet = df_sheet.where(pd.notnull(df_sheet), None)
        return df_sheet.to_dict()