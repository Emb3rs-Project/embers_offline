import ast

class ReadDataMM:

    def get_data(self, df_file_excel):
        bm_data = self.get_bm_data(df_file_excel["BM"])

        return bm_data

    def get_bm_data(self, df_sheet):
        df_sheet = df_sheet[["Input name", "CS Input"]]
        df_sheet = df_sheet.set_index('Input name')
        df_sheet["CS Input"] = ast.literal_eval(df_sheet["CS Input"])
        df_sheet.index.name = None

        df_sheet = df_sheet.transpose()
        return df_sheet.to_dict()

