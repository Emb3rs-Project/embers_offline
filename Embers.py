import os
from src.Simulations.DHN.DHNAssessment import DHNAssessment
from src.Simulations.Internal_Heat_Recovery.DesignORC import DesignORC
from src.Simulations.Internal_Heat_Recovery.PinchAnalysis import PinchAnalysis

# Main
class Embers:

    def run_dhn(self, dhn_file,output_folder,not_to_run_modules=[]):
        dhn = DHNAssessment(not_to_run_modules)
        dhn.read_user_inputs(dhn_file)
        dhn.run_simulation()
        dhn.get_reports(output_folder)

    # TODO: NOT YET FINISHED
    #def run_design_orc(self, orc_file, output_folder):
    #    orc = DesignORC()
    #    orc.read_user_inputs(orc_file)
    #    orc.run_simulation()
    #    orc.get_reports(output_folder)

    #def run_pinch_analysis(self, pinch_file,output_folder):
    #    pinch = PinchAnalysis()
    #    pinch.read_user_inputs(pinch_file)
    #    pinch.run_simulation()
    #    pinch.get_reports(output_folder)
#
#############################################################################################
#############################################################################################
# USER INTERACTION -> Users have to put the correct file name to be read on the "test" folder.

# Dummy
# Get file
dhn_excel_file = os.path.abspath('test/inputs/dhn_data.xlsx')
#orc_excel_file = os.path.abspath('test/inputs/orc_data.xlsx')
#pinch_excel_file = os.path.abspath('test/inputs/pinch_data.xlsx')

## Save outputs in this folder
output_folder = os.path.abspath('test/outputs/')

## Run platform features - As simple as that
platform = Embers()
platform.run_dhn(dhn_excel_file, output_folder)
#platform.run_pinch_analysis(pinch_excel_file, output_folder)
#platform.run_design_orc(pinch_excel_file, output_folder)

