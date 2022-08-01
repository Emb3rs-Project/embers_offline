"""
test function that makes input datastructures, then applies market functions
for p2p market with CO2 preferences, and block offers,
and with all other settings to default.

"""

# import own modules
from ...short_term.market_functions.run_shortterm_market import run_shortterm_market


def test_p2p_co2():
    # TEST P2P co2#################################################################################
    # setup inputs --------------------------------------------
    print("running test_p2p_co2().............................................")
    # TEST P2P #######################################################################################
    input_dict = {#'sim_name': 'test_p2p_co2',
                  'md': 'p2p',  # other options are  'p2p' or 'community'
                  'nr_of_hours': 12,
                  'offer_type': 'block',
                  'prod_diff': 'co2Emissions',
                  'network': 'none',
                  'el_dependent': 'false',  # can be false or true
                  'el_price': 'none',
                  'agent_ids': ["prosumer_1",
                                "prosumer_2", "consumer_1", "producer_1"],
                  'objective': 'none',  # objective for community
                  'community_settings': {'g_peak': 'none', 'g_exp': 'none', 'g_imp': 'none'},
                  'gmin': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                           [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                           [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  'gmax': [[1, 2, 0, 5], [3, 4, 0, 4], [1, 5, 0, 3], [0, 0, 0, 0], [1, 1, 0, 1],
                           [2, 3, 0, 1], [4, 2, 0, 5], [3, 4, 0, 4], [1, 5, 0, 3],
                           [0, 0, 0, 0], [1, 1, 0, 1], [2, 3, 0, 1]],
                  'lmin': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                           [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                           [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  'lmax': [[2, 2, 1, 0], [2, 1, 0, 0], [1, 2, 1, 0], [3, 0, 2, 0], [1, 1, 4, 0],
                           [2, 3, 3, 0], [4, 2, 1, 0], [3, 4, 2, 0], [1, 5, 3, 0], [0, 0, 5, 0],
                           [1, 1, 3, 0], [2, 3, 1, 0]],
                  'cost': [[24, 25, 45, 30], [31, 24, 0, 24], [18, 19, 0, 32], [0, 0, 0, 0],
                           [20, 25, 0, 18], [25, 31, 0, 19], [24, 27, 0, 22], [32, 31, 0, 19],
                           [15, 25, 0, 31], [0, 0, 0, 0], [19, 20, 0, 21], [22, 33, 0, 17]],
                  'util': [[40, 42, 35, 25], [45, 50, 40, 0], [55, 36, 45, 0], [44, 34, 43, 0],
                           [34, 44, 55, 0], [29, 33, 45, 0], [40, 55, 33, 0],
                           [33, 42, 38, 0], [24, 55, 35, 0], [25, 35, 51, 0], [19, 43, 45, 0], [34, 55, 19, 0]],
                  'co2_emissions': [1, 1.1, 0, 1.8],
                  'is_in_community': 'none',  # allowed values are 'none' or boolean array of size (nr_of_agents)
                  'block_offer': {'prosumer_1': [[0, 1]], 'producer_1': [[3, 4, 5, 6], [10, 11]]},
                  'is_chp': 'none',  # allowed values are 'none' or a list with ids of agents that are CHPs
                  'chp_pars': 'none',
                   'gis_data':
                      {'from_to': ['("prosumer_1", "prosumer_2")', '("prosumer_2", "consumer_1")', '("prosumer_2", "producer_1")'],
                       'losses_total': [22969.228855, 24122.603833, 18138.588662],
                       'length': [1855.232413, 1989.471069, 1446.688900],
                       'total_costs': [1.848387e+06, 1.934302e+06, 1.488082e+06]},
                  'nodes' : "none",
                  'edges' : "none"
                  }

    result_dict = run_shortterm_market(input_dict=input_dict)

    # MAIN RESULTS

    # Shadow price per hour
    print(result_dict['shadow_price'])

    # Energy dispatch
    print(result_dict['Pn'])

    # Settlement
    print(result_dict['settlement'])

    # Social welfare
    print(result_dict['social_welfare_h'])

    # Quality of Experience (QoE)
    print(result_dict['QoE'])

    print("finished test_p2p_co2().............................................")