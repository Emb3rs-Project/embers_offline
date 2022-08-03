def mapping_bm_internal_heat_recovery(cf_data):
    bm_data = {
        "capex": cf_data["best_options[].capex"],
        "O & M_fix": cf_data["best_options[].om_fix"],
        "duration": cf_data["best_options[].lifetime"],
        "money_Sav": cf_data["best_options[].money_savings"],
        "energy_dispatch": cf_data["best_options[].energy_dispatch"],
        "disocunt_rate": cf_data["best_options[].discount_rate"],
        "carbon_sav_quant": cf_data["best_options[].co2_savings"],
    }
    return bm_data