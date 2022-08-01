import ast

class ReadDataTEO:

    def get_data(self, df_file_excel):
        teo_sets_data = self.get_teo_sets_data(df_file_excel["TEO - Sets"])
        teo_storages_data = self.get_teo_storages_data(df_file_excel["TEO - Storages"])
        teo_emissions_data = self.get_teo_emissions_data(df_file_excel["TEO - Annual Emission Limit"])

        teo_data = {}


        teo_data.update(teo_sets_data)
        teo_data.update(teo_storages_data)
        teo_data.update(teo_emissions_data)



        return teo_data


    def get_teo_sets_data(self, df_sheet):
        df_sheet = df_sheet[["Variable", "CS Input"]]
        df_sheet = df_sheet.set_index('Variable')
        data = df_sheet['CS Input'].to_dict()

        data["REGION"] = str(data["REGION"])
        data["EMISSION"] = str(data["EMISSION"])
        data["TIMESLICE"] = ast.literal_eval(data["TIMESLICE"])
        data["YEAR"] = ast.literal_eval(data["YEAR"])
        data["MODE_OF_OPERATION"] = ast.literal_eval(data["MODE_OF_OPERATION"])
        data["STORAGE"] = data["STORAGE"].strip('][').split(', ')
        data["platform_budget_limit"] = float(data["platform_budget_limit"])

        new_data = {"platform_sets": data}

        return self.clean_dict(new_data)


    def get_teo_storages_data(self, df_sheet):

        df_sheet = df_sheet.drop(columns=['Storage Data', '-', 'Unit'])
        df_sheet = df_sheet.set_index('Variable')


        data = df_sheet['Storage'].to_dict()

        data["dicount_rate_sto"] = float(data["dicount_rate_sto"])
        data["operational_life_sto"] = float(data["operational_life_sto"])

        data = df_sheet.to_dict()
        data = [value for (key,value) in data.items()]
        new_data = {"platform_storages": data}

        return self.clean_dict(new_data)


    def get_teo_emissions_data(self, df_sheet):
        df_sheet = df_sheet[["Emission", "Value"]]
        df_sheet.rename(columns={'Emission': 'emission', 'Value': 'annual_emission_limit'}, inplace=True)
        data = df_sheet.transpose().to_dict()
        data = [value for (key,value) in data.items() ]

        new_data = {"platform_annual_emission_limit": data}

        return self.clean_dict(new_data)


    def clean_dict(self,dict):
        # NOTE: UPDATE THIS

        clean_dict = dict
        return clean_dict