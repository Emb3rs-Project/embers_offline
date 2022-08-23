
def mapping_convert_sinks(sinks,gis_data):

    data ={
            "platform": {"group_of_sinks": sinks,
                         "grid_supply_temperature": gis_data["flow_temp"],
                         "grid_return_temperature": gis_data["return_temp"]
                        }

    }

    return data