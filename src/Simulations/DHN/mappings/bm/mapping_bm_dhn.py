

def mapping_bm_dhn(teo_data, mm_data, gis_data, user_data):

    bm_data = {
        "teo-module": {
            "DiscountedCapitalInvestmentByTechnology": teo_data["DiscountedCapitalInvestmentByTechnology"],
            "DiscountedCapitalInvestmentByStorage": teo_data["DiscountedCapitalInvestmentByStorage"],
            "DiscountedSalvageValueByTechnology": teo_data["DiscountedSalvageValueByTechnology"],
            "DiscountedSalvageValueByStorage":  teo_data["DiscountedSalvageValueByStorage"],
            "TotalDiscountedFixedOperatingCost": teo_data["TotalDiscountedFixedOperatingCost"]
        },

        "market-module": {
            "shadow_price": mm_data["results"]["shadow_price"],
            "Pn": mm_data["results"]["Pn"],
            "agent_operational_cost": mm_data["results"]["agent_operational_cost"],
        },

        "gis-module": {
            "net_cost": gis_data["sums"]["total_costs"],
        },
        "platform": {
            "rls": user_data["rls"],
            "discountrate_i": user_data["discount_rate"],
            "projectduration": user_data["project_duration"],
            "actorshare": user_data["actorshare"],
            "co2_intensity": user_data["co2_intensity"]
        }
    }

    return bm_data




