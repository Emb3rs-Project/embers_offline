from cf_module.src.Source.simulation.Heat_Recovery.ORC.convert_orc import convert_orc


class DesignORC:

    def read_user_inputs(self, file):
        cf_inputs = ReadDataCF()
        self.cf_data_raw = cf_inputs.get_data(file)

    def run_simulation(self):
        self.pinch_analysis_results = convert_orc(self.cf_data_raw)

    def get_reports(self):
        file = open("pinch_analysis_results.html", "w")
        file.write(self.pinch_analysis_results["report"])
        file.close()