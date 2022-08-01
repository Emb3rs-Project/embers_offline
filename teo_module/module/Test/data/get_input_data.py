import json
import os


def get_input_data():
    input_data_file = open(
        os.path.join(os.path.dirname(__file__), "input_data.json"), "r"
    )
    return json.load(input_data_file)
