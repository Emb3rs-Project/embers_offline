import json

from ..Test.prepare_inputs import prepare_inputs
from .TEO_Model import buildmodel
from .utilities import (
    create_parameters_dataframe,
    create_parameters_default_dataframe,
    create_sets_dataframe,
)
from .kb import kb


def run_build_model(input_data):

    sets_df, df, default_df = _prepare_inputs(input_data)

    model_output = buildmodel(sets_df, df, default_df, None, 0)

    return _prepare_outputs(model_output)


def _prepare_inputs(input_data):

    gis_module = input_data["gis-module"]
    cf_module = input_data["cf-module"]
    platform = input_data["platform"]

    default_df = create_parameters_default_dataframe(kb["parameters_default"])
    jsset = platform["platform_sets"]
    jsset["TECHNOLOGY"] = cf_module["sets_technologies"]
    jsset["FUEL"] = cf_module["sets_fuels"]

    sets_df = create_sets_dataframe(jsset)

    df = create_parameters_dataframe(sets_df, default_df)

    df = prepare_inputs(sets_df, df, input_data)

    return sets_df, df, default_df


def _prepare_outputs(output_data):

    output = open("./output.json", "w")
    json.dump(output_data, output)

    return output_data
