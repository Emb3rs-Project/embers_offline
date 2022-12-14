import json


def gis_module_to_buildmodel(river_data):
    optimize_network = river_data["optimize_network"]
    return {
        "losses_in_kw": optimize_network["losses_cost_kw"]["losses_in_kw"],
        "cost_in_kw": optimize_network["losses_cost_kw"]["cost_in_kw"],
    }


def cf_module_to_buildmodel_sets_technologies(river_data):
    output = []
    river_convert_sink = river_data["convert_sink"]
    river_convert_source = river_data["convert_source"]

    output.append(river_convert_source["teo_string"])

    for sink in river_convert_sink["all_sinks_info"]["sinks"]:
        for stream in sink["streams"]:
            for conversion_technology in stream["conversion_technologies"]:
                output.append(conversion_technology["teo_equipment_name"])

    for grid in river_convert_sink["all_sinks_info"]["grid_specific"]:
        output.append(grid["teo_equipment_name"])

    for source in river_convert_source["all_sources_info"]:
        for stream in source["streams_converted"]:
            output.append(stream["teo_stream_id"])
            for conversion_technology in stream["conversion_technologies"]:
                output.append(conversion_technology["teo_equipment_name"])

    return list(filter(lambda x: (x is not None), output))


def cf_module_to_buildmodel_sets_fuels(river_data):
    output = []
    river_convert_sink = river_data["convert_sink"]
    river_convert_source = river_data["convert_source"]

    output.append(river_convert_source["teo_dhn"]["input_fuel"])
    output.append(river_convert_source["teo_dhn"]["output_fuel"])

    for source in river_convert_source["all_sources_info"]:
        for stream in source["streams_converted"]:
            output.append(stream["input_fuel"])
            output.append(stream["output_fuel"])

            for conversion_technology in stream["conversion_technologies"]:
                output.append(conversion_technology["input_fuel"])
                output.append(conversion_technology["output_fuel"])

    for grid in river_convert_sink["all_sinks_info"]["grid_specific"]:
        output.append(grid["input_fuel"])
        output.append(grid["output_fuel"])

    for sink in river_convert_sink["all_sinks_info"]["sinks"]:
        for stream in sink["streams"]:
            output.append(stream["demand_fuel"])
            for conversion_technology in stream["conversion_technologies"]:
                output.append(conversion_technology["input_fuel"])
                output.append(conversion_technology["output_fuel"])

    return list(dict.fromkeys(list(filter(lambda x: (x is not None), output))))


def cf_module_to_buildmodel_specified_annual_demand_cf(river_data):
    output = []
    river_convert_sink = river_data["convert_sink"]

    for sink in river_convert_sink["all_sinks_info"]["sinks"]:
        for stream in sink["streams"]:
            output.append(
                {"fuel": stream["demand_fuel"], "value": stream["teo_yearly_demand"]}
            )

    return list(filter(lambda x: (x is not None), output))


def create_technology_cf(river_data, props):

    river_convert_source = river_data["convert_source"]
    return river_convert_source["teo_dhn"] | props


def cf_module_to_buildmodel_technologies_cf(river_data):
    output = []
    river_convert_sink = river_data["convert_sink"]
    river_convert_source = river_data["convert_source"]

    output.append(create_technology_cf(river_data=river_data, props={}))

    for sink in river_convert_sink["all_sinks_info"]["sinks"]:
        for stream in sink["streams"]:
            for conversion_technology in stream["conversion_technologies"]:

                cond_input = {}
                if "input" in conversion_technology.keys():
                    cond_input["input"] = conversion_technology["input"]

                cond_technology = {}
                if "teo_equipment_name" in conversion_technology.keys():
                    cond_technology["technology"] = conversion_technology[
                        "teo_equipment_name"
                    ]

                output.append(
                    create_technology_cf(
                        river_data=river_data,
                        props={
                                  "input_fuel": conversion_technology["input_fuel"],
                                  "output_fuel": conversion_technology["output_fuel"],
                                  "output": conversion_technology["output"],
                                  "max_capacity": conversion_technology["max_capacity"],
                                  "turnkey_a": conversion_technology["turnkey_a"],
                                  "om_fix": conversion_technology["om_fix"],
                                  "om_var": conversion_technology["om_var"],
                                  "emissions_factor": conversion_technology["emissions"],
                                  "input": conversion_technology["conversion_efficiency"],
                              }
                              | cond_input
                              | cond_technology,
                    )
                )

    for grid in river_convert_sink["all_sinks_info"]["grid_specific"]:

        cond_input = {}
        if "input" in grid.keys():
            cond_input["input"] = grid["input"]

        cond_technology = {}
        if "teo_equipment_name" in grid.keys():
            cond_technology["technology"] = grid["teo_equipment_name"]

        output.append(
            create_technology_cf(
                river_data=river_data,
                props={
                          "input_fuel": grid["input_fuel"],
                          "output_fuel": grid["output_fuel"],
                          "output": grid["output"],
                          "max_capacity": grid["max_capacity"],
                          "turnkey_a": grid["turnkey_a"],
                          "om_fix": grid["om_fix"],
                          "om_var": grid["om_var"],
                          "emissions_factor": grid["emissions"],
                      }
                      | cond_input
                      | cond_technology,
            )
        )

    for source in river_convert_source["all_sources_info"]:
        for stream in source["streams_converted"]:
            cond_input = {}
            if "input" in stream.keys():
                cond_input["input"] = stream["input"]

            cond_technology = {}
            if "teo_equipment_name" in stream.keys():
                cond_technology["technology"] = stream["teo_equipment_name"]
            elif "teo_stream_id" in stream.keys():
                cond_technology["technology"] = stream["teo_stream_id"]

            output.append(
                create_technology_cf(
                    river_data=river_data,
                    props={
                              "input_fuel": None,
                              "output_fuel": stream["output_fuel"],
                              "output": stream["output"],
                              "max_capacity": stream["max_stream_capacity"],
                              "turnkey_a": 0,
                              "om_fix": 0,
                              "om_var": 0,
                              "emissions_factor": 0,
                          }
                          | cond_input
                          | cond_technology,
                )
            )

            for conversion_technology in stream["conversion_technologies"]:

                cond_input = {}
                if "input" in conversion_technology.keys():
                    cond_input["input"] = conversion_technology["input"]

                cond_technology = {}
                if "teo_equipment_name" in conversion_technology.keys():
                    cond_technology["technology"] = conversion_technology[
                        "teo_equipment_name"
                    ]

                output.append(
                    create_technology_cf(
                        river_data=river_data,
                        props={
                                  "input_fuel": conversion_technology["input_fuel"],
                                  "output_fuel": conversion_technology["output_fuel"],
                                  "output": conversion_technology["output"],
                                  "max_capacity": conversion_technology["max_capacity"],
                                  "turnkey_a": conversion_technology["turnkey_a"],
                                  "om_fix": conversion_technology["om_fix"],
                                  "om_var": conversion_technology["om_var"],
                                  "emissions_factor": conversion_technology["emissions"],
                                  "input": conversion_technology["conversion_efficiency"],
                              }
                              | cond_input
                              | cond_technology,
                    )
                )
    for row in output:
        if row["input_fuel"] is None:
            row["input_fuel"] = ""

    return output


def cf_module_to_buildmodel(river_data):
    river_convert_sink = river_data["convert_sink"]
    river_convert_source = river_data["convert_source"]

    return {
        "specified_demand_profile_cf": river_convert_sink["teo_demand_factor_group"],
        "sets_technologies": cf_module_to_buildmodel_sets_technologies(
            river_data=river_data
        ),
        "sets_fuels": cf_module_to_buildmodel_sets_fuels(river_data=river_data),
        "technologies_cf": cf_module_to_buildmodel_technologies_cf(
            river_data=river_data
        ),
        "specified_annual_demand_cf": cf_module_to_buildmodel_specified_annual_demand_cf(
            river_data=river_data
        ),
        "capacity_factor_cf": river_convert_source["teo_capacity_factor_group"],
    }


def create_default_technology(name):
    return {
        "technology": name,
        "availability_factor": 0.95,
        "discount_rate_tech": 0.04,
        "capacity_to_activity": 8761,
        "residual_capacity": 0,
        "max_capacity_investment": 100000000000,
        "min_capacity": 0,
        "min_capacity_investment": 0,
        "annual_activity_lower_limit": 0,
        "annual_activity_upper_limit": 100000000000,
        "model_period_activity_lower_limit": 0,
        "model_period_activity_upper_limit": 1500000000000,
    }


def platform_technologies_to_buildmodel(river_data):
    return list(
        map(
            lambda x: create_default_technology(x),
            cf_module_to_buildmodel_sets_technologies(river_data=river_data),
        )
    )



def platform_technology_to_storage_to_build_model(river_data):
    data = []
    for storage in river_data["platform_storages"]:
        data.append({
            "technology": "dhn",
            "storage": storage["storage"],
            "technologytostorage": 1,
            "technologyfromstorage": 1,
        })
    return data

def platform_to_buildmodel(river_data):
    platform_technologies = platform_technologies_to_buildmodel(river_data=river_data)

    platform_technology_to_storage_data = platform_technology_to_storage_to_build_model(river_data)

    return {
        "platform_technologies": platform_technologies,
        "platform_sets": river_data["platform_sets"],
        "platform_storages": river_data["platform_storages"],
        "platform_annual_emission_limit": river_data["platform_annual_emission_limit"],
        "platform_budget_limit": [{"Region": "Sweden", "budget_limit": 10000000000000}],
        "platform_technology_to_storage": platform_technology_to_storage_data
    }



def mapping_teo(optimize_network_data, convert_sinks_data, convert_sources_data,user_inputs):

    river_data = {
        "optimize_network": optimize_network_data,
        "convert_sink": convert_sinks_data,
        "convert_source": convert_sources_data}

    river_data.update(user_inputs)

    _gis_module_to_buildmodel = gis_module_to_buildmodel(river_data)
    _cf_module_to_buildmodel = cf_module_to_buildmodel(river_data)
    _platform_to_buildmodel = platform_to_buildmodel(river_data)


    return {"platform": _platform_to_buildmodel, "gis-module":_gis_module_to_buildmodel, "cf-module": _cf_module_to_buildmodel}
