from numpy import floor, inner
import pandas as pd
from pandas.core.frame import DataFrame
from .gen_settings import DEFAULT_PARAM_SETTINGS


def create_sets_dataframe(jData):

    # SETS (LOAD FROM JSON)
    jData["DAYTYPE"] = []
    jData["SEASON"] = []
    jData["DAILYTIMEBRACKET"] = []
    jData["FLEXIBLEDEMANDTYPE"] = []
    jData["REGION2"] = []

    sets_df = {}

    sets_df["REGION"] = pd.DataFrame(jData["REGION"], columns=["REGION"], dtype=str)
    sets_df["REGION2"] = pd.DataFrame(jData["REGION2"], columns=["REGION2"], dtype=str)
    sets_df["DAYTYPE"] = pd.DataFrame(jData["DAYTYPE"], columns=["DAYTYPE"], dtype=str)
    sets_df["EMISSION"] = pd.DataFrame(
        jData["EMISSION"], columns=["EMISSION"], dtype=str
    )
    sets_df["FUEL"] = pd.DataFrame(jData["FUEL"], columns=["FUEL"], dtype=str)
    sets_df["DAILYTIMEBRACKET"] = pd.DataFrame(
        jData["DAILYTIMEBRACKET"], columns=["DAILYTIMEBRACKET"], dtype=str
    )
    sets_df["SEASON"] = pd.DataFrame(jData["SEASON"], columns=["SEASON"], dtype=str)
    sets_df["TIMESLICE"] = pd.DataFrame(
        jData["TIMESLICE"], columns=["TIMESLICE"], dtype=str
    )
    sets_df["MODE_OF_OPERATION"] = pd.DataFrame(
        jData["MODE_OF_OPERATION"], columns=["MODE_OF_OPERATION"], dtype=str
    )
    sets_df["STORAGE"] = pd.DataFrame(jData["STORAGE"], columns=["STORAGE"], dtype=str)
    sets_df["TECHNOLOGY"] = pd.DataFrame(
        jData["TECHNOLOGY"], columns=["TECHNOLOGY"], dtype=str
    )
    sets_df["YEAR"] = pd.DataFrame(jData["YEAR"], columns=["YEAR"], dtype=str)
    sets_df["FLEXIBLEDEMANDTYPE"] = pd.DataFrame(
        jData["FLEXIBLEDEMANDTYPE"], columns=["FLEXIBLEDEMANDTYPE"], dtype=str
    )

    return sets_df


def create_parameters_dataframe(sets_df, default_df):

    # PARAMETERS (GENERATE)~

    default_columns = [
        "PARAM",
        "VALUE",
        "REGION",
        "REGION2",
        "DAYTYPE",
        "EMISSION",
        "FUEL",
        "DAILYTIMEBRACKET",
        "SEASON",
        "TIMESLICE",
        "STORAGE",
        "MODE_OF_OPERATION",
        "TECHNOLOGY",
        "YEAR",
    ]

    df = pd.DataFrame(columns=default_columns)

    for index, row in default_df.iterrows():
        value_default = row["VALUE"]
        param = row["PARAM"]

        # Count Values
        count = 1
        for column in DEFAULT_PARAM_SETTINGS[param]:
            inner_count = 0
            for _ in sets_df[column][column]:
                inner_count = inner_count + 1

            count = count * inner_count

        gen_param = {}
        for i in range(count):
            gen_param[i] = {"PARAM": param, "VALUE": value_default}

        acc_repeat = 1
        for column in DEFAULT_PARAM_SETTINGS[param]:
            set_value_len = len(sets_df[column][column])

            for index in range(count):
                pos = floor(index / acc_repeat) % set_value_len
                gen_param[index][column] = sets_df[column][column][pos]

            acc_repeat = acc_repeat * set_value_len

        gen_df = pd.DataFrame(gen_param).transpose()
        df = df.append(gen_df)
        # ACTIVATE BREAK FOR ONLY FIRST PARAMETER OF DEFAULT_PARAMETERS
        #break

    return df


def create_parameters_default_dataframe(jData):

    # PARAMETERS_DEFAULT (LOAD FROM JSON)

    defaults_df = pd.DataFrame(jData)
    defaults_df.fillna(0)

    defaults_df["PARAM"] = defaults_df["PARAM"].astype(str)
    defaults_df["VALUE"] = defaults_df["VALUE"].apply(pd.to_numeric, downcast="signed")

    return defaults_df
