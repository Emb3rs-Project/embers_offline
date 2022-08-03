

def mapping_bm_dhn(teo_data, mm_data, gis_data, user_data):

    capex_tt = []
    capex_t_names = []
    capex_st = []
    capex_s_names = []
    sal_tt = []
    sal_st = []
    opex_tt = []

    for i in range(0, len(teo_data["DiscountedCapitalInvestmentByTechnology"])):
        capex_tt.append(teo_data["DiscountedCapitalInvestmentByTechnology"][i]["VALUE"])
        capex_t_names.append(teo_data["DiscountedCapitalInvestmentByTechnology"][i]["TECHNOLOGY"])

    for i in range(0, len(teo_data["DiscountedCapitalInvestmentByStorage"])):
        capex_st.append(teo_data["DiscountedCapitalInvestmentByStorage"][i]["VALUE"])
        capex_s_names.append(teo_data["DiscountedCapitalInvestmentByStorage"][i]["STORAGE"])

    for i in range(0, len(teo_data["DiscountedSalvageValueByTechnology"])):
        sal_tt.append(teo_data["DiscountedSalvageValueByTechnology"][i]["VALUE"])

    for i in range(0, len(teo_data["DiscountedSalvageValueByStorage"])):
        sal_st.append(teo_data["DiscountedSalvageValueByStorage"][i]["VALUE"])

    for i in range(0, len(teo_data["TotalDiscountedFixedOperatingCost"])):
        opex_tt.append(teo_data["TotalDiscountedFixedOperatingCost"][i]["VALUE"])


    bm_data = {
        "teo-module": {
            "capex_tt": capex_tt, # teo_data["DiscountedCapitalInvestmentByTech"]["VALUE"]
            "capex_t_names": capex_t_names, # teo_data["DiscountedCapitalInvestmentByTech"]["TECHNOLOGY"]
            "capex_st": capex_st, # teo_data["DiscountedCapitalInvestmentByStorage"]["VALUE"]
            "capex_s_names": capex_s_names, # teo_data["DiscountedCapitalInvestmentByStorage"]["TECHNOLOGY"]
            "sal_tt": sal_tt, # teo_data["DiscountedSalvageValueByTech"]["VALUE"]
            "sal_st": sal_st, # teo_data["DiscountedSalvageValueByStorage"]["VALUE"]
            "opex_tt": opex_tt, # teo_data["TotalDiscountedFixedOperatingCost"]["VALUE"]
        },

        "mm-module": {
            "price_h": mm_data["shadow_price"],
            "Dispatch_ah": mm_data["Pn"],
            "op_cost_i": mm_data["agent_operation_cost"],
        },

        "gis-module": {
            "net_cost": gis_data["sums"]["total_costs"],
        },
        "platform": {
            "rls": user_data["rls"],
            "discountrate_i": user_data["discount_rate"],
            "projectduration": user_data["project_duration"],
            "actorshare": user_data["actorshare"],
            "co2_intensity": user_data["co2_intensity"],
            #"gdrown":user_data["gdrown"]
        }
    }

    return bm_data




