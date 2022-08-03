from .Simulations.DHN.DHNAssessment import DHNAssessment
from .Simulations.Internal_Heat_Recovery.DesignORC import DesignORC
from .Simulations.Internal_Heat_Recovery.PinchAnalysis import PinchAnalysis

class Embers:

    def run_dhn(self, dhn_file):
        dhn = DHNAssessment()
        dhn.read_user_inputs(dhn_file)
        dhn.run_simulation()
        dhn.get_reports()

    def run_design_orc(self, orc_file):
        orc = DesignORC()
        orc.read_user_inputs(orc_file)
        orc.run_simulation()
        orc.get_reports()

    def run_pinch_analysis(self, pinch_file):
        pinch = PinchAnalysis()
        pinch.read_user_inputs(pinch_file)
        pinch.run_simulation()
        pinch.get_reports()

####################################################################################

# get file
dhn_excel_file = '../test/dhn_data.xlsx'

# platform
platform = Embers()
platform.run_dhn(dhn_excel_file)
# platform.pinch_analysis()
# platform.design_orc()
