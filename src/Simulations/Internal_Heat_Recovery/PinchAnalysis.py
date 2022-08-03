from ....cf_module.src.Source.simulation.Heat_Recovery.convert_pinch_isolated_streams import convert_pinch_isolated_streams
from .read_data.read_pinch import ReadDataPinchIsolatedStreams
from ....cf_module.src.utilities.kb import KB
from ....cf_module.src.utilities.kb_data import kb
from .mappings.mapping_pinch_isolated_streams import mapping_pinch_isolated_streams

class PinchAnalysis:

    def read_user_inputs(self, file):
        cf_inputs = ReadDataPinchIsolatedStreams()
        self.cf_data_raw = cf_inputs.get_data(file)

    def run_simulation(self):
        pinch_analysis_input = mapping_pinch_isolated_streams(self.cf_data_raw)
        self.pinch_analysis_results = convert_pinch_isolated_streams(pinch_analysis_input, KB(kb))

    def get_reports(self):
        file = open("pinch_analysis_results.html", "w")
        file.write(self.pinch_analysis_results ["report"])
        file.close()