import ast

class ReadDataGIS:

    def get_data(self, df_file_excel):
        gis_data = self.get_gis_data(df_file_excel["GIS"])
        return gis_data

    def get_gis_data(self,df_sheet):

        df_sheet = df_sheet[["Variable", "CS Input"]].copy()
        df_sheet[2:]["CS Input"] = df_sheet.loc[2:]["CS Input"].apply(float)

        df_sheet = df_sheet.set_index('Variable')
        data = df_sheet["CS Input"].to_dict()

        data["polygon"] = ast.literal_eval(data["polygon"])

        return self.clean_dict(data)


    def clean_dict(self,dict):
        # NOTE: UPDATE THIS

        clean_dict = dict
        return clean_dict