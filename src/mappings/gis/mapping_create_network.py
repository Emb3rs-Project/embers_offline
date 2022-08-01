
def mapping_create_network(user_data, convert_sinks_data, convert_sources_data, teo_data):


    data = {
        "platform": {
            "ex_grid": [],
            "network_resolution": user_data["network_resolution"],
            "polygon": user_data["polygon"],
        },
        "cf-module": {
            "n_supply_list": convert_sources_data["n_supply_list"],
            "n_demand_list": convert_sinks_data["n_demand_list"],
            "n_grid_specific": convert_sinks_data["n_grid_specific"],
            "n_thermal_storage": convert_sinks_data["n_thermal_storage"],
        },
        "teo-module": {
            "ex_cap": teo_data["ex_capacities"]
        },
    }


    return data