import json
import pandas as pd
import os


from .data.get_input_data import get_input_data
from .prepare_inputs import *

from ..src.integration import run_build_model

def run_test():
    input_data = get_input_data()

    result = run_build_model(input_data=input_data)

    print(result)
    # MCS and N are not needed
    # buildmodel(sets_df, df, default_df, None, 0)
