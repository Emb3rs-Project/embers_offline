import ast

class ReadDataBM:

    def get_data(self, df_file_excel):
        bm_data = self.get_bm_data(df_file_excel["BM"])

        return bm_data

    def get_bm_data(self, df_sheet):
        df_sheet = df_sheet[["Input name", "CS Input"]]
        df_sheet = df_sheet.set_index('Input name')

        df_sheet.loc["discount_rate","CS Input"] = ast.literal_eval(df_sheet.loc["discount_rate","CS Input"])
        df_sheet.loc["project_duration","CS Input"] = int(df_sheet.loc["project_duration","CS Input"])
        df_sheet.loc["co2_intensity","CS Input"] = float(df_sheet.loc["co2_intensity","CS Input"])
        df_sheet.loc["actorshare","CS Input"] = ast.literal_eval(df_sheet.loc["actorshare","CS Input"])
        df_sheet.loc["rls","CS Input"] = ast.literal_eval(df_sheet.loc["rls","CS Input"])

        data = df_sheet.transpose().to_dict(orient='records')[0]

        return data

