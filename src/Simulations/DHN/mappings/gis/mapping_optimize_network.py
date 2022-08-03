
def mapping_optimize_network(user_input, create_network_data, convert_sources_data, convert_sinks_data, teo_data={"ex_cap":[]}):

    data = {
        "gis-module": {
            "nodes": create_network_data["nodes"],
            "edges": create_network_data["edges"],
            "demand_list": create_network_data["demand_list"],
            "supply_list": create_network_data["supply_list"],
        },
        "platform": {
            "ex_grid": [],
            "network_resolution": user_input["network_resolution"],
            "water_den": user_input["water_den"],
            "factor_street_terrain": user_input["factor_street_terrain"],
            "factor_street_overland": user_input["factor_street_overland"],
            "heat_capacity": user_input["heat_capacity"],
            "flow_temp": user_input["flow_temp"],
            "return_temp": user_input["return_temp"],
            "surface_losses_dict": [],
            "ground_temp": user_input["ground_temp"],
            "ambient_temp": user_input["ambient_temp"],
            "fc_dig_st": user_input["fc_dig_st"],
            "vc_dig_st": user_input["vc_dig_st"],
            "vc_dig_st_ex": user_input["vc_dig_st_ex"],
            "fc_dig_tr": user_input["fc_dig_tr"],
            "vc_dig_tr": user_input["vc_dig_tr"],
            "vc_dig_tr_ex": user_input["vc_dig_tr_ex"],
            "fc_pip": user_input["fc_pip"],
            "vc_pip": user_input["vc_pip"],
            "vc_pip_ex": user_input["vc_pip_ex"],
            "invest_pumps": user_input["invest_pumps"],
        },
        "cf-module": {
            "n_supply_list": convert_sources_data["n_supply_list"],
            "n_demand_list": convert_sinks_data["n_demand_list"]
        },

        "teo-module": {"ex_cap": teo_data["ex_cap"]},
    }

    return data
