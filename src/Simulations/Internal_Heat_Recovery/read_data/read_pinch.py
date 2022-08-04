import pandas as pd
import numpy as np

class ReadDataPinchIsolatedStreams:

    def get_data(self, file):

        df_file = pd.read_excel(file, sheet_name=None)

        for sheet in df_file.keys():
            df_file[sheet] = self.clean_df(df_file[sheet])
            df_file[sheet] = df_file[sheet].replace({np.nan:None})

        streams_data = self.get_streams(df_file["CF - Streams Data"])
        fuels_data = self.get_fuels_data(df_file["CF - Fuels Data"])
        general_data = self.get_general_data(df_file["CF - General Data"])

        return {"streams": streams_data,
                "fuels_data": fuels_data,
                "pinch_delta_T_min": general_data["pinch_delta_T_min"],
                "location":[general_data['latitude'],general_data['longitude']],
                "interest_rate":general_data["interest_rate"]}


    def get_general_data(self, df_sheet):
        return df_sheet.to_dict(orient='records')[0]


    def get_streams(self,df_sheet):
        streams_data = df_sheet.replace({np.nan: None})

        streams_data = streams_data.to_dict(orient='records')

        streams_updated = []
        for stream in streams_data:
            stream = {key_stream: self.get_parameters_values(key_stream, value_stream) for (key_stream, value_stream)
                             in stream.items() if value_stream != None}
            streams_updated.append(stream)


        return streams_updated

    def get_fuels_data(self, df_sheet):

        df_sheet = df_sheet.set_index('fuel')

        df_sheet["price"] = df_sheet["price"]/1000
        df_sheet.index.name = None
        df_sheet = df_sheet.transpose()
        df_sheet = df_sheet.where(pd.notnull(df_sheet), None)
        return df_sheet.to_dict()


    def clean_df(self,df_sheet):

        df_sheet.rename(columns=df_sheet.iloc[0], inplace=True)
        df_sheet = df_sheet.iloc[2:]

        return df_sheet


    def get_parameters_values(self, key, val):
        import ast
        new_val = {
            "saturday_on": {"yes": 1, "no": 0},
            "sunday_on": {"yes": 1, "no": 0},
            "space_heating_type": {"Conventional": 1, "Low temperature": 2},
            "building_orientation": {
                                    "North": "N",
                                    "South": "S",
                                    "East": "E",
                                    "West": "W"},
        }

        if key == "real_hourly_capacity" or key == "real_monthly_capacity":
            val = ast.literal_eval(val)
            return val

        elif key in new_val:
            return new_val[key][val]
        else:
            return val
