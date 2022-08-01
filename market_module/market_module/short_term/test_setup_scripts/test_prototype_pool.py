"""
script that makes input datastructures, then applies market functions
"""
import json
import numpy as np
import pandas as pd
import os
import sys
import datetime

# import own modules
from ...short_term.datastructures.inputstructs import AgentData, MarketSettings, Network
from ...short_term.market_functions.pool_market import make_pool_market
from ...short_term.market_functions.p2p_market import make_p2p_market

# import own modules
from ...short_term.market_functions.run_shortterm_market import run_shortterm_market

dummy = True

# TEST POOL #######################################################################################
# setup inputs --------------------------------------------
user_input = {'md': 'pool',
              'offer_type': 'simple',
              'prod_diff': 'noPref', 
              "network": 'none',
              "el_dependent": 'false',
              'nr_of_hours': 2,
              "objective": 'none', 
              "community_settings": {'g_peak': 'none', 'g_exp': 'none', 'g_imp': 'none'}, 
              "block_offer": 'none',
              "is_in_community" : 'none', 
              "chp_pars": 'none', 
              "el_price": 'none',  ## THIS WILL ONLY BE AS USER INPUT!!!
              "start_datetime": "31-01-2002",
              "util": {"1_2": [0.40, 0.42],
                       "56_2": [0.45, 0.50]}
            }
# extract day month year------------------
day, month, year = [int(x) for x in user_input["start_datetime"].split("-")]
as_date = datetime.datetime(year=year, month=month, day=day)
start_hourofyear = as_date.timetuple().tm_yday * 24 
end_hourofyear = start_hourofyear + user_input["nr_of_hours"]

# TODO get GIS data ----------
if dummy:
    gis_data = "none"

# read TEO file --------------
fn = "/home/linde/Documents/2019PhD/EMB3Rs/module_integration/AccumulatedNewCapacity.json"
f = open(fn, "r")
teo_vals = json.load(f)

# make a dummy teo output
teo_output = {"AccumulatedNewCapacity": teo_vals, "AnnualVariableOperatingCost": teo_vals, 
                "ProductionByTechnologyAnnual": teo_vals, "AnnualTechnologyEmission" : teo_vals}

# extract TEO info
AccumulatedNewCapacity = pd.json_normalize(teo_output["AccumulatedNewCapacity"])
#type(AccumulatedNewCapacity.YEAR[0])
AccumulatedNewCapacity["YEAR"] = AccumulatedNewCapacity["YEAR"].astype(int)
#type(AccumulatedNewCapacity.YEAR[0])

AnnualVariableOperatingCost = pd.json_normalize(teo_output["AnnualVariableOperatingCost"])
AnnualVariableOperatingCost["YEAR"] = AnnualVariableOperatingCost["YEAR"].astype(int)
ProductionByTechnologyAnnual = pd.json_normalize(teo_output["ProductionByTechnologyAnnual"])
ProductionByTechnologyAnnual["YEAR"] = ProductionByTechnologyAnnual["YEAR"].astype(int)

# year must be one of the years that the TEO simulates for
if not year in AccumulatedNewCapacity.YEAR.to_list():
    ValueError("User chosen 'year' must be one of the YEARs provided by TEO")



# extract source names -------------------
source_names = AccumulatedNewCapacity.TECHNOLOGY.unique()
nr_of_sources = len(source_names)

# prep inputs
lmax_sources = np.zeros((user_input["nr_of_hours"], nr_of_sources))
util_sources = np.zeros((user_input["nr_of_hours"], nr_of_sources))
gmax_sources = np.array([AccumulatedNewCapacity.loc[(AccumulatedNewCapacity['YEAR'] == year) & 
                 (AccumulatedNewCapacity['TECHNOLOGY'] == x)].VALUE.to_list()[0] for x in source_names])
gmax_sources = np.reshape(gmax_sources, (1, nr_of_sources))
gmax_sources = np.repeat(gmax_sources, user_input["nr_of_hours"], axis=0)
cost_sources = np.array(
                [AnnualVariableOperatingCost.loc[(AnnualVariableOperatingCost['YEAR'] == year) & 
                 (AnnualVariableOperatingCost['TECHNOLOGY'] == x)].VALUE.to_list()[0] /
                 ProductionByTechnologyAnnual.loc[(ProductionByTechnologyAnnual['YEAR'] == year) & 
                 (ProductionByTechnologyAnnual['TECHNOLOGY'] == x)].VALUE.to_list()[0]                 
                 for x in source_names])
cost_sources = np.reshape(cost_sources, (1, nr_of_sources))
cost_sources = np.repeat(cost_sources, user_input["nr_of_hours"], axis=0)

# TODO get CO2 emissions from TEO 
if dummy:
    co2_em = "none" # np.zeros(())

# TODO get CF data for is_chp?
if dummy:
    is_chp = "none" # np.zeros(())


# get CF sink data --------------------------
fncf2 = "/home/linde/Documents/2019PhD/EMB3Rs/module_integration/convert_sinks.jsonc"
f = open(fncf2, "r")
all_sinks_info = json.load(f)
all_sinks_info = all_sinks_info["all_sinks_info"]["sinks"]

# get some sink info 
nr_of_sinks = len(all_sinks_info)
sink_ids = []
sink_locs = []
map_sink_streams = []

for i in range(nr_of_sinks):
    sink_ids += [all_sinks_info[i]["sink_id"]]
    sink_locs += [all_sinks_info[i]["location"]]
    map_sink_streams += [[streams["stream_id"] for streams in all_sinks_info[i]["streams"]]]

# get some stream info 
all_stream_ids = [y for x in map_sink_streams for y in x]
nr_of_streams = len(all_stream_ids)
timesteps = len(all_sinks_info[0]["streams"][0]["hourly_stream_capacity"])

# prep inputs
lmax_sinks = np.zeros((user_input["nr_of_hours"], nr_of_streams))
counter = 0 
for j in range(nr_of_sinks):
    for i in range(len(map_sink_streams[j])):
        if dummy:
            all_sinks_info[j]["streams"][i]["hourly_stream_capacity"] = (
                all_sinks_info[j]["streams"][i]["hourly_stream_capacity"] * 400*20)[1:8784]
        # 

        lmax_sinks[:, counter] = all_sinks_info[j]["streams"][i]["hourly_stream_capacity"][start_hourofyear:end_hourofyear]
        counter += 1

gmax_sinks = np.zeros(np.shape(lmax_sinks))
cost_sinks = np.zeros(np.shape(lmax_sinks))
util_sinks = [user_input["util"][x] for x in all_stream_ids]


# make input dict ------------------------
# combine source and sink inputs
agent_ids = list(source_names) + all_stream_ids

gmax = np.concatenate((gmax_sources, gmax_sinks), axis=1).tolist()
lmax = np.concatenate((gmax_sources, lmax_sinks), axis=1).tolist()
cost = np.concatenate((cost_sources, cost_sinks), axis=1).tolist()
util = np.concatenate((util_sources, util_sinks), axis=1).tolist()


# construct input_dict
input_dict = {
                  'md': user_input['md'],  # other options are  'p2p' or 'community'
                  'nr_of_hours': user_input["nr_of_hours"],
                  'offer_type': user_input["offer_type"],
                  'prod_diff': user_input["prod_diff"],
                  'network': user_input["network"],
                  'el_dependent': user_input["el_dependent"],  # can be false or true
                  'el_price': user_input["el_price"],
                  'agent_ids': agent_ids,
                  'objective': user_input["objective"],  # objective for community
                  'community_settings': user_input["community_settings"], 
                  'gmax': gmax,
                  'lmax': lmax,
                  'cost': cost,
                  'util': util,
                  'co2_emissions': co2_em,  # allowed values are 'none' or array of size (nr_of_agents)
                  'is_in_community': user_input["is_in_community"],  # allowed values are 'none' or boolean array of size (nr_of_agents)
                  'block_offer': user_input["block_offer"],
                  'is_chp': is_chp, #user_input["is_chp"],  # allowed values are 'none' or a list with ids of agents that are CHPs
                  'chp_pars': user_input["chp_pars"],
                  'gis_data': gis_data
                  }

result_dict = run_shortterm_market(input_dict=input_dict)

# MAIN RESULTS

# Shadow price per hour
print(result_dict['shadow_price'])

# Energy dispatch
print(result_dict['Pn'])

# Energy dispatch
print(result_dict['Tnm'])

# Settlement
print(result_dict['settlement'])

# Social welfare
print(result_dict['social_welfare_h'])

# Quality of Experience (QoE)
print(result_dict['QoE'])