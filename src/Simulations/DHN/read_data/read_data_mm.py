import ast

class ReadDataMM:

    def get_data(self, df_file_excel):
        mm_data = self.get_mm_data(df_file_excel["MARKET"])

        return mm_data

    def get_mm_data(self,df_sheet):
        df_sheet = df_sheet[['input name', "CS Input"]]
        df_sheet = df_sheet.set_index('input name')
        df_sheet.loc['util',"CS Input"] = ast.literal_eval(df_sheet.loc['util',"CS Input"])
        df_sheet.index.name = None

        return df_sheet['CS Input'].to_dict()

