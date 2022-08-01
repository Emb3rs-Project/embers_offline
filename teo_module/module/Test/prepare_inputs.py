import json
import pandas as pd
import os
import itertools
import warnings
import numpy
import itertools
from ..src.error_handling.Validation import *

def prepare_inputs(sets_df, df, input_data):
    input_platform = input_data["platform"]
    input_gis = input_data["gis-module"]
    input_cf = input_data["cf-module"]
    import pandas as pd
    sets_df = sets_df
    df = df
    technologies_cf = pd.DataFrame(input_cf['technologies_cf'])
    specified_annual_demand_cf = pd.DataFrame(input_cf['specified_annual_demand_cf'])
    specified_demand_profile_cf = pd.DataFrame(input_cf['specified_demand_profile_cf'])
    capacity_factor_cf = pd.DataFrame(input_cf['capacity_factor_cf'])
    platform_technologies= pd.DataFrame(input_platform['platform_technologies'])
    platform_storages = pd.DataFrame(input_platform['platform_storages'])
    platform_annual_emission_limit = pd.DataFrame(input_platform['platform_annual_emission_limit'])
    platform_technology_to_storage = pd.DataFrame(input_platform['platform_technology_to_storage'])
    platform_budget_limit= pd.DataFrame(input_platform['platform_budget_limit'])
    
    sets_df1_year = pd.DataFrame(sets_df['YEAR'])
    sets_df1_storage = pd.DataFrame(sets_df['STORAGE'])
    sets_df1_tech = pd.DataFrame(sets_df['TECHNOLOGY'])
    sets_df1_mode_of_operation = pd.DataFrame(sets_df['MODE_OF_OPERATION'])
    technologies_cf = pd.DataFrame(input_cf['technologies_cf'])
    # SETS CHECK

    STOLIST =  sets_df1_storage["STORAGE"].tolist()
    MOOLIST =  sets_df1_mode_of_operation["MODE_OF_OPERATION"].tolist()

    if len(STOLIST) != 0 and len(MOOLIST) != 2:
        raise Exception("Please make sure that there are two modes of operation if Storage is used in the model")
    elif  len(MOOLIST) == 0:
        raise Exception("Please make sure that there is atleast one mode of operation used in the model")

    #Parameters check

    maxcapinvestment = platform_technologies["max_capacity_investment"].tolist()
    mincapinvestment = platform_technologies["min_capacity_investment"].tolist()
    mincap = platform_technologies["min_capacity"].tolist()
    annactlowlim = platform_technologies["annual_activity_lower_limit"].tolist()
    annactupplim = platform_technologies["annual_activity_upper_limit"].tolist()
    modperactlowlim = platform_technologies["model_period_activity_lower_limit"].tolist()
    modperactupplim = platform_technologies["model_period_activity_upper_limit"].tolist()
    rescap =  platform_technologies["residual_capacity"].tolist()
    maxcap = technologies_cf["max_capacity"].tolist()
    techlist = platform_technologies["technology"].tolist()
    resstocap =  platform_storages["residual_storage_capacity"].tolist()
    maxstocap = platform_storages["max_storage_capacity"].tolist()
    stolevelstart = platform_storages["storage_level_start"].tolist()
    yearlist = sets_df1_year["YEAR"].tolist()
    stolist = platform_storages["storage"].tolist()
    STOLIST =  sets_df1_storage["STORAGE"].tolist()
    MOOLIST =  sets_df1_mode_of_operation["MODE_OF_OPERATION"].tolist()
    listcf = technologies_cf.columns.values.tolist()
    listcfcheck = ['input_fuel','output_fuel','output','max_capacity','turnkey_a','om_fix','om_var','emissions_factor','input','technology','emissions','emission','conversion_efficiency']
    setstechlist = sets_df1_tech["TECHNOLOGY"].tolist()
    cftechlist = technologies_cf["technology"].tolist()
    listspd = specified_annual_demand_cf["fuel"].tolist()
    listspdprof = specified_demand_profile_cf.columns.values.tolist()
    print(listspdprof)
    listcfcap = capacity_factor_cf.columns.values.tolist()
    
    masterdict = {}
    masterdict["maxcapinvestment"] = maxcapinvestment
    masterdict["mincapinvestment"] = mincapinvestment
    masterdict["mincap"] = mincap
    masterdict["annactlowlim"] = annactlowlim
    masterdict["annactupplim"] = annactupplim
    masterdict["modperactlowlim"] = modperactlowlim
    masterdict["modperactupplim"] = modperactupplim
    masterdict["rescap"] = rescap
    masterdict["maxcap"] = maxcap
    masterdict["techlist"] = techlist
    masterdict["resstocap"] = resstocap
    masterdict["maxstocap"] = maxstocap
    masterdict["stolevelstart"] = stolevelstart
    masterdict["yearlist"] = yearlist
    masterdict["stolist"] = stolist
    masterdict["STOLIST"] = STOLIST
    masterdict["MOOLIST"] = MOOLIST
    masterdict["listcf"] = listcf
    masterdict["listcfcheck"] = listcfcheck
    masterdict["setstechlist"] = setstechlist
    masterdict["cftechlist"] = cftechlist
    masterdict["listspd"] = listspd
    masterdict["listspdprof"] = listspdprof
    masterdict["listcfcap"] = listcfcap
    
    Inputscheck(**masterdict)




    # BudgetLimit
#     df5567 = platform_budget_limit
#     budget_list199 = df5567["budget_limit"]
#     df2576 = df.loc[df["PARAM"] == "MaximumBudget"]
#     region_list2233 = df2576["REGION"].tolist()

#     Assign1 = []

#     for i in range(0, len(region_list2233)):
#         a = budget_list199[i]
#         b = -9999999999 + a
#         if  a != 0:
#             Assign1.append(b)
#         else:
#             Assign1.append(0)

#     Assign1
#     df2576["Assignment"] = Assign1
#     sum_column = df2576["Assignment"] + df2576["VALUE"]
#     df2576["SUM"] = sum_column
#     df2576
#     df2576.drop("VALUE", axis=1, inplace=True)
#     df2576.drop("Assignment", axis=1, inplace=True)
#     df2576.rename(columns={"SUM": "VALUE"}, inplace=True)
#     df2576
#     df2576 = df2576[
#         [
#             "PARAM",
#             "VALUE",
#             "REGION",
#             "REGION2",
#             "DAYTYPE",
#             "EMISSION",
#             "FUEL",
#             "DAILYTIMEBRACKET",
#             "SEASON",
#             "TIMESLICE",
#             "STORAGE",
#             "MODE_OF_OPERATION",
#             "TECHNOLOGY",
#             "YEAR",
#         ]
#     ]
#     df = df.loc[df["PARAM"] != "MaximumBudget"]
#     df = df.reset_index(drop=True)
#     df2576 = df2576.reset_index(drop=True)
#     df = df.append(df2576, ignore_index=True)
    
    # GIS_LOSSES
    df555 = input_gis
    loss_list198 = df555["losses_in_kw"]
    df1 = df.loc[df["PARAM"] == "GIS_Losses"]
    Fuel_list1 = df1["FUEL"].tolist()
    Assign1 = []
    Fuel_list1

    for x in Fuel_list1:
        if ("dhnwaterdem") in x:
            Assign1.append(loss_list198)
        else:
            Assign1.append(0)

    Assign1
    df1["Assignment"] = Assign1
    df1.drop("VALUE", axis=1, inplace=True)
    df1.rename(columns={"Assignment": "VALUE"}, inplace=True)
    df1 = df1[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "GIS_Losses"]
    df = df.reset_index(drop=True)
    df1 = df1.reset_index(drop=True)
    df = df.append(df1, ignore_index=True)

    # OAR
    df483 = pd.DataFrame(input_cf["technologies_cf"])
    Tech_list198 = df483["technology"].tolist()
    Value_list198 = df483["output"].tolist()
    Fuel_list198 = df483["output_fuel"].tolist()
    df3 = df.loc[df["PARAM"] == "OutputActivityRatio"]
    Tech_list3 = df3["TECHNOLOGY"].tolist()
    Tech_list3d = []
    Tech_list3
    for i in Tech_list3:
        if i not in Tech_list3d:
            Tech_list3d.append(i)

    Fuel_list3 = df3["FUEL"].tolist()
    Fuel_list3d = []

    for j in Fuel_list3:
        if j not in Fuel_list3d:
            Fuel_list3d.append(j)

    Year_list3 = df3["YEAR"].tolist()
    Year_list3d = []

    for k in Year_list3:
        if k not in Year_list3d:
            Year_list3d.append(k)

    MO_list3 = df3["MODE_OF_OPERATION"].tolist()
    MO_list3d = []

    for l in MO_list3:
        if l not in MO_list3d:
            MO_list3d.append(l)

    maxcounter2 = len(MO_list3d) * len(Year_list3d)
    maxcounter2
    Assign3 = []
    Assign3f = []
    Assign3t = []
    Assign3m = []
    Assign3y = []
    Counter = []
    CounterY = []
    identifier = []
    Assignedcounter = []
    for o in range(0, len(Tech_list198)):
        identifier.append(str(Fuel_list198[o] + Tech_list198[o]))
        

    for j in range(0, len(Tech_list198)):
        a3 = Value_list198[j]
        b3 = Tech_list198[j]
        c3 = Fuel_list198[j]

        for x in Fuel_list3d:
            for w in MO_list3d:
                for y in Tech_list3d:
                    for z in Year_list3d:
                        Counterstring = str(str(x) + str(y))
                        if ((b3) in y and (c3) in x) and (Assignedcounter.count(Counterstring) < maxcounter2):
                            if ((int(w) == 1)):
                                Assign3.append(a3)
                                Assign3f.append(x)
                                Assign3m.append(w)
                                Assign3t.append(y)
                                Assign3y.append(z)
                                Assignedcounter.append(Counterstring)

                            elif((int(w) != 1)):
                                Assign3.append(0)
                                Assign3f.append(x)
                                Assign3m.append(w)
                                Assign3t.append(y)
                                Assign3y.append(z)
                        elif (
                            (b3 not in y and c3 not in x)
                             and (Counterstring not in identifier)
                            and (Counter.count(Counterstring) < maxcounter2)
                        ):
                            Assign3.append(0)
                            Assign3f.append(x)
                            Assign3m.append(w)
                            Assign3t.append(y)
                            Assign3y.append(z)
                        elif (
                            (b3 not in y or c3 not in x)
                            and (Counterstring not in identifier)
                            and Counter.count(Counterstring) < maxcounter2
                        ):
                            Assign3.append(0)
                            Assign3f.append(x)
                            Assign3m.append(w)
                            Assign3t.append(y)
                            Assign3y.append(z)
                        Counter.append(Counterstring)

    df3["Assignment"] = Assign3
    df3["Assignmentf"] = Assign3f
    df3["Assignmentm"] = Assign3m
    df3["Assignmentt"] = Assign3t
    df3["Assignmenty"] = Assign3y
    sum_column = df3["Assignment"] + df3["VALUE"]
    df3["SUM"] = sum_column
    df3.drop("VALUE", axis=1, inplace=True)
    df3.drop("TECHNOLOGY", axis=1, inplace=True)
    df3.drop("MODE_OF_OPERATION", axis=1, inplace=True)
    df3.drop("YEAR", axis=1, inplace=True)
    df3.drop("FUEL", axis=1, inplace=True)
    df3.drop("Assignment", axis=1, inplace=True)
    df3.rename(columns={"SUM": "VALUE"}, inplace=True)
    df3.rename(columns={"Assignmentf": "FUEL"}, inplace=True)
    df3.rename(columns={"Assignmentm": "MODE_OF_OPERATION"}, inplace=True)
    df3.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df3.rename(columns={"Assignmenty": "YEAR"}, inplace=True)
    df3 = df3[
        [
        "PARAM",
        "VALUE",
        "REGION",
        "REGION2",
        "DAYTYPE",
        "EMISSION",
        "FUEL",
        "DAILYTIMEBRACKET",
        "SEASON",
        "TIMESLICE",
        "STORAGE",
        "MODE_OF_OPERATION",
        "TECHNOLOGY",
        "YEAR",
    ]
    ]
    df3 = df3.reset_index(drop=True)
    df = df.loc[df["PARAM"] != "OutputActivityRatio"]
    df = df.reset_index(drop=True)
    df = df.append(df3, ignore_index=True)



    # IAR
    df482 = technologies_cf
    Tech_list197 = df482["technology"].tolist()
    Value_list197 = df482["input"].tolist()
    Fuel_list197 = df482["input_fuel"].tolist()

    df1256 = platform_technology_to_storage
    Tech_list1232 = df1256["technology"].tolist()


    df4 = df.loc[df["PARAM"] == "InputActivityRatio"]

    Tech_list1971 = []
    Fuel_list1971 = []
    Value_list1971 = []
    for l in range(len(Fuel_list197)):
        if (Fuel_list197[l] != ''):
            Tech_list1971.append(Tech_list197[l])
            Fuel_list1971.append(Fuel_list197[l])
            Value_list1971.append(Value_list197[l])

    Tech_list197 = Tech_list1971
    Value_list197 = Value_list1971
    Fuel_list197 = Fuel_list1971
    Tech_list4 = df4["TECHNOLOGY"].tolist()
    Tech_list4d = []

    for i in Tech_list4:
        if i not in Tech_list4d:
            Tech_list4d.append(i)

    Fuel_list4 = df4["FUEL"].tolist()
    Fuel_list4d = []

    for j in Fuel_list4:
        if j not in Fuel_list4d:
            Fuel_list4d.append(j)

    Year_list4 = df4["YEAR"].tolist()
    Year_list4d = []

    for k in Year_list4:
        if k not in Year_list4d:
            Year_list4d.append(k)

    MO_list4 = df4["MODE_OF_OPERATION"].tolist()
    MO_list4d = []

    for l in MO_list4:
        if l not in MO_list4d:
            MO_list4d.append(l)

    maxcounter1 = len(MO_list4d) * len(Year_list4d)

    Assign4 = []
    Assign4f = []
    Assign4t = []
    Assign4m = []
    Assign4y = []
    Counter = []
    identifier1 = []
    Assignedcounter1 = []
    for o in range(0, len(Tech_list197)):
        identifier1.append(str(Fuel_list197[o] + Tech_list197[o]))
        

    for j in range(0, len(Tech_list197)):

        a4 = Value_list197[j]
        b4 = Tech_list197[j]
        c4 = Fuel_list197[j]

        for x in Fuel_list4d:
            for w in MO_list4d:
                for y in Tech_list4d:
                    for z in Year_list4d:
                        Counterstring = str(str(x) + str(y))
                        if (b4 in y and c4 in x) and (Assignedcounter1.count(Counterstring) < maxcounter1):
                            if b4 in Tech_list1232 and int(w) == 2:
                            #print(str(str(x) + str(y)))
                                Assign4.append(a4)
                                Assign4f.append(x)
                                Assign4m.append(w)
                                Assign4t.append(y)
                                Assign4y.append(z)
                                Assignedcounter1.append(Counterstring)

                            elif b4 not in Tech_list1232 and int(w) == 2:
                                #print(str(str(x) + str(y)))
                                Assign4.append(0)
                                Assign4f.append(x)
                                Assign4m.append(w)
                                Assign4t.append(y)
                                Assign4y.append(z)

                            elif b4 in Tech_list1232 and int(w) == 1:
                                #print(str(str(x) + str(y)))
                                Assign4.append(0)
                                Assign4f.append(x)
                                Assign4m.append(w)
                                Assign4t.append(y)
                                Assign4y.append(z)

                            elif b4 not in Tech_list1232 and int(w) == 1:
                                #print(str(str(x) + str(y)))
                                Assign4.append(a4)
                                Assign4f.append(x)
                                Assign4m.append(w)
                                Assign4t.append(y)
                                Assign4y.append(z)
                                Assignedcounter1.append(Counterstring)

                        elif (b4 not in y and c4 not in x) and (Counterstring not in identifier1) and Counter.count(
                            Counterstring
                        ) < maxcounter1:
                            #print(str(str(x) + str(y)))
                            Assign4.append(0)
                            Assign4f.append(x)
                            Assign4m.append(w)
                            Assign4t.append(y)
                            Assign4y.append(z)
                        elif (b4 not in y or c4 not in x) and (Counterstring not in identifier1) and Counter.count(
                            Counterstring
                        ) < maxcounter1:
                            #print(str(str(x) + str(y)))
                            Assign4.append(0)
                            Assign4f.append(x)
                            Assign4m.append(w)
                            Assign4t.append(y)
                            Assign4y.append(z)
                        Counter.append(Counterstring)

    df4["Assignment"] = Assign4
    df4["Assignmentf"] = Assign4f
    df4["Assignmentm"] = Assign4m
    df4["Assignmentt"] = Assign4t
    df4["Assignmenty"] = Assign4y
    sum_column = df4["Assignment"] + df4["VALUE"]
    df4["SUM"] = sum_column
    df4.drop("VALUE", axis=1, inplace=True)
    df4.drop("TECHNOLOGY", axis=1, inplace=True)
    df4.drop("MODE_OF_OPERATION", axis=1, inplace=True)
    df4.drop("YEAR", axis=1, inplace=True)
    df4.drop("FUEL", axis=1, inplace=True)
    df4.drop("Assignment", axis=1, inplace=True)
    df4.rename(columns={"SUM": "VALUE"}, inplace=True)
    df4.rename(columns={"Assignmentf": "FUEL"}, inplace=True)
    df4.rename(columns={"Assignmentm": "MODE_OF_OPERATION"}, inplace=True)
    df4.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df4.rename(columns={"Assignmenty": "YEAR"}, inplace=True)
    df4 = df4[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df4 = df4.reset_index(drop=True)
    df = df.loc[df["PARAM"] != "InputActivityRatio"]
    df = df.reset_index(drop=True)
    df = df.append(df4, ignore_index=True)
    
    # CFCAPITALCOSTS
    import itertools
    df482 = technologies_cf
    Tech_list197 = df482["technology"].tolist()
    Value_list197 = df482["turnkey_a"].tolist()
    Assign5 = []
    Assign5t = []

    df5 = df.loc[df["PARAM"] == "CapitalCost"]
    df5
    Tech_list5 = df5["TECHNOLOGY"].tolist()
    Tech_list5

    Year_list5 = df5["YEAR"].tolist()
    Year_list5d = []

    for i in Year_list5:
        if i not in Year_list5d:
            Year_list5d.append(i)
    counter5 = []
    maxcounter5 = len(Year_list5d)
    for j in range(0, len(Tech_list197)): 

        a5 = Value_list197[j] + 0.01

        b5 = Tech_list197[j]

        for y in Tech_list5:
            counterstring5 = str(y)
            if b5 in y:
                Assign5.append(a5)
                Assign5t.append(y)
            elif (b5 not in y) and (y not in Tech_list197) and (counter5.count(counterstring5) < maxcounter5):
                Assign5.append(0.01)
                Assign5t.append(y)
            counter5.append(counterstring5)
    len(df5)
    df5["Assignment"] = Assign5
    df5["Assignmentt"] = Assign5t
    sum_column = df5["Assignment"] + df5["VALUE"]
    df5["SUM"] = sum_column
    df5.drop("VALUE", axis=1, inplace=True)
    df5.drop("TECHNOLOGY", axis=1, inplace=True)
    df5.drop("Assignment", axis=1, inplace=True)
    df5.rename(columns={"SUM": "VALUE"}, inplace=True)
    df5.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df5 = df5[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "CapitalCost"]
    df = df.reset_index(drop=True)
    df5 = df5.reset_index(drop=True)
    df = df.append(df5, ignore_index=True)

    # GISCAPITALCOSTS
    df556 = input_gis
    cost_list199 = df556["cost_in_kw"]
    df2 = df.loc[df["PARAM"] == "CapitalCost"]
    Tech_list2 = df2["TECHNOLOGY"].tolist()

    Assign1 = []

    for y in Tech_list2:
        if (",".join(["dhn"])) in y:
            Assign1.append(cost_list199)
        else:
            Assign1.append(0)

    Assign1
    df2["Assignment"] = Assign1
    sum_column = df2["Assignment"] + df2["VALUE"]
    df2["SUM"] = sum_column
    df2
    df2.drop("VALUE", axis=1, inplace=True)
    df2.drop("Assignment", axis=1, inplace=True)
    df2.rename(columns={"SUM": "VALUE"}, inplace=True)
    df2 = df2[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "CapitalCost"]
    df = df.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)
    df = df.append(df2, ignore_index=True)
    
    # CFFIXEDCOSTS
    df481 = technologies_cf
    Tech_list196 = df481["technology"].tolist()
    Value_list196 = df481["om_fix"].tolist()
    Assign6 = []
    Assign6t = []
    df6 = df.loc[df["PARAM"] == "FixedCost"]

    Tech_list6 = df6["TECHNOLOGY"].tolist()
    Tech_list6

    Year_list6 = df6["YEAR"].tolist()
    Year_list6d = []

    for i in Year_list6:
        if i not in Year_list6d:
            Year_list6d.append(i)
    counter6 = []
    maxcounter6 = len(Year_list6d)
    for j in range(0, len(Tech_list196)):

        a6 = Value_list196[j]

        b6 = Tech_list196[j]

        for y in Tech_list6:
            counterstring6 = str(y)
            if str(b6) in y:
                Assign6.append(a6)
                Assign6t.append(y)
            elif (b6 not in y) and (y not in Tech_list196) and (counter6.count(counterstring6) < maxcounter6):
                Assign6.append(0)
                Assign6t.append(y)
            counter6.append(counterstring6)
    len(Assign6)
    df6["Assignment"] = Assign6
    df6["Assignmentt"] = Assign6t
    sum_column = df6["Assignment"] + df6["VALUE"]
    df6["SUM"] = sum_column
    df6.drop("VALUE", axis=1, inplace=True)
    df6.drop("TECHNOLOGY", axis=1, inplace=True)
    df6.drop("Assignment", axis=1, inplace=True)
    df6.rename(columns={"SUM": "VALUE"}, inplace=True)
    df6.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df6 = df6[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "FixedCost"]
    df = df.reset_index(drop=True)
    df6 = df6.reset_index(drop=True)
    df = df.append(df6, ignore_index=True)
    df

    # CFMAXCAPACITY
    df480 = technologies_cf
    Tech_list196 = df480["technology"].tolist()
    Tech_list196
    Value_list196 = df480["max_capacity"].tolist()
    Assign7 = []
    Assign7t = []
    df7 = df.loc[df["PARAM"] == "TotalAnnualMaxCapacity"]

    Tech_list7 = df7["TECHNOLOGY"].tolist()
    Tech_list7

    Year_list7 = df7["YEAR"].tolist()
    Year_list7d = []

    for i in Year_list7:
        if i not in Year_list7d:
            Year_list7d.append(i)

    counter7 = []
    maxcounter7 = len(Year_list7d)
    for j in range(0, len(Tech_list196)):

        a7 = -999999999 + Value_list196[j]
        b7 = Tech_list196[j]

        for y in Tech_list7:
            counterstring7 = str(y)
            if str(b7) in y:
                Assign7.append(a7)
                Assign7t.append(y)
            elif (b7 not in y) and (y not in Tech_list196) and (counter7.count(Counterstring7) < maxcounter7):
                Assign7.append(0)
                Assign7t.append(y)
            counter7.append(counterstring7)
    df7["Assignment"] = Assign7
    df7["Assignmentt"] = Assign7t
    sum_column = df7["Assignment"] + df7["VALUE"]
    df7["SUM"] = sum_column
    df7.drop("VALUE", axis=1, inplace=True)
    df7.drop("TECHNOLOGY", axis=1, inplace=True)
    df7.drop("Assignment", axis=1, inplace=True)
    df7.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df7.rename(columns={"SUM": "VALUE"}, inplace=True)
    df7 = df7[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "TotalAnnualMaxCapacity"]
    df = df.reset_index(drop=True)
    df7 = df7.reset_index(drop=True)
    df = df.append(df7, ignore_index=True)
    df
    
    # CFVARCOST
    df490 = technologies_cf
    Tech_list198 = df490["technology"].tolist()
    Value_list198 = df490["om_var"].tolist()
    Assign7 = []
    df8 = df.loc[df["PARAM"] == "VariableCost"]

    Tech_list8 = df8["TECHNOLOGY"].tolist()
    Tech_list8d = []

    for i in Tech_list8:
        if i not in Tech_list8d:
            Tech_list8d.append(i)

    Year_list8 = df8["YEAR"].tolist()
    Year_list8d = []

    for k in Year_list8:
        if k not in Year_list8d:
            Year_list8d.append(k)

    MO_list8 = df8["MODE_OF_OPERATION"].tolist()
    MO_list8d = []
    Assign8 = []
    Assign8t = []
    Assign8m = []
    Assign8y = []
    Counter8 = []
    maxcounter8 = len(MO_list8d) * len(Year_list8d)
    for l in MO_list8:
        if l not in MO_list8d:
            MO_list8d.append(l)

    for j in range(0, len(Tech_list198)):

        a8 = Value_list198[j]
        b8 = Tech_list198[j]

        for w in MO_list8d:
            for y in Tech_list8d:
                for z in Year_list8d:
                    Counterstring8 = str(y)
                    if ((b8) in y) and (int(w) == 1):
                        Assign8.append(a8)
                        Assign8m.append(w)
                        Assign8t.append(y)
                        Assign8y.append(z)
                    elif (b8 in y) and (int(w) != 1):
                        Assign8.append(0)
                        Assign8m.append(w)
                        Assign8t.append(y)
                        Assign8y.append(z)  
                    elif (b8 not in y) and (y not in Tech_list198) and Counter8.count(Counterstring8) < maxcounter8:
                        Assign8.append(0)
                        Assign8m.append(w)
                        Assign8t.append(y)
                        Assign8y.append(z)
                    Counter8.append(Counterstring8)

    df8["Assignment"] = Assign8
    df8["Assignmentm"] = Assign8m
    df8["Assignmentt"] = Assign8t
    df8["Assignmenty"] = Assign8y                                    
    sum_column = df8["Assignment"] + df8["VALUE"]
    df8["SUM"] = sum_column
    df8.drop("VALUE", axis=1, inplace=True)
    df8.drop("TECHNOLOGY", axis=1, inplace=True)
    df8.drop("MODE_OF_OPERATION", axis=1, inplace=True)
    df8.drop("YEAR", axis=1, inplace=True)                                    
    df8.drop("Assignment", axis=1, inplace=True)
    df8.rename(columns={"SUM": "VALUE"}, inplace=True)
    df8.rename(columns={"Assignmentm": "MODE_OF_OPERATION"}, inplace=True)
    df8.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df8.rename(columns={"Assignmenty": "YEAR"}, inplace=True)

    df8 = df8[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "VariableCost"]
    df = df.reset_index(drop=True)
    df8 = df8.reset_index(drop=True)
    df = df.append(df8, ignore_index=True)

    # EmissionsAR
    df491 = technologies_cf
    EM_list199 = df491["emissions"]
    Value_list199 = df491["emissions_factor"].tolist()
    Tech_list199 = df491["technology"].tolist()
    Assign9 = []
    Assign9e = []
    Assign9t = []
    Assign9m = []
    Assign9y = []
    df9 = df.loc[df["PARAM"] == "EmissionActivityRatio"]
    Tech_list9 = df9["TECHNOLOGY"].tolist()
    Tech_list9d = []

    for i in Tech_list9:
        if i not in Tech_list9d:
            Tech_list9d.append(i)

    Emission_list9 = df9["EMISSION"].tolist()
    Emission_list9d = []

    for j in Emission_list9:
        if j not in Emission_list9d:
            Emission_list9d.append(j)

    Year_list9 = df9["YEAR"].tolist()
    Year_list9d = []

    for k in Year_list9:
        if k not in Year_list9d:
            Year_list9d.append(k)

    MO_list9 = df9["MODE_OF_OPERATION"].tolist()
    MO_list9d = []

    for l in MO_list9:
        if l not in MO_list9d:
            MO_list9d.append(l)

    Counter9 = []
    maxcounter9 = len(MO_list9d) * len(Year_list9d)
    identifier9 = []

    for o in range(0, len(Tech_list199)):
        identifier9.append(str(EM_list199[o] + Tech_list199[o]))

    for j in range(0, len(Tech_list199)):

        a9 = Value_list199[j]
        b9 = Tech_list199[j]
        c9 = EM_list199[j]

        for x in Emission_list9d:
            for w in MO_list9d:
                for y in Tech_list9d:
                    for z in Year_list9d:
                        Counterstring9 = str(str(x) + str(y))
                        if (b9 in y) and (c9 in x) and (int(w) == 1):
                            Assign9.append(a9)
                            Assign9e.append(x)
                            Assign9m.append(w)
                            Assign9t.append(y)
                            Assign9y.append(z)

                        elif ((b9 in y) and (c9  in x)) and (int(w) != 1):
                            Assign9.append(0)
                            Assign9e.append(x)
                            Assign9m.append(w)
                            Assign9t.append(y)
                            Assign9y.append(z)

                        elif ((b9 not in y) or (c9 not in x)) and (Counterstring9 not in identifier9) and (Counter9.count(Counterstring9) < maxcounter9):
                            Assign9.append(0)
                            Assign9e.append(x)
                            Assign9m.append(w)
                            Assign9t.append(y)
                            Assign9y.append(z)
                        Counter9.append(Counterstring9) 

    len(Assign9)
    df9["Assignment"] = Assign9
    df9["Assignmente"] = Assign9e
    df9["Assignmentm"] = Assign9m
    df9["Assignmentt"] = Assign9t
    df9["Assignmenty"] = Assign9y
    sum_column = df9["Assignment"] + df9["VALUE"]
    df9["SUM"] = sum_column
    df9
    df9.drop("VALUE", axis=1, inplace=True)
    df9.drop("TECHNOLOGY", axis=1, inplace=True)
    df9.drop("MODE_OF_OPERATION", axis=1, inplace=True)
    df9.drop("YEAR", axis=1, inplace=True)
    df9.drop("EMISSION", axis=1, inplace=True)
    df9.drop("Assignment", axis=1, inplace=True)
    df9.rename(columns={"SUM": "VALUE"}, inplace=True)
    df9.rename(columns={"Assignmente": "EMISSION"}, inplace=True)
    df9.rename(columns={"Assignmentm": "MODE_OF_OPERATION"}, inplace=True)
    df9.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df9.rename(columns={"Assignmenty": "YEAR"}, inplace=True)
    df9 = df9[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "EmissionActivityRatio"]
    df = df.reset_index(drop=True)
    df9 = df9.reset_index(drop=True)
    df = df.append(df9, ignore_index=True)

    # SpecifiedAnnualDemand
    df472 = specified_annual_demand_cf
    Fuel_list177 = df472["fuel"].tolist()
    Fuel_list177
    Value_list177 = df472["value"].tolist()
    Assign10 = []
    df10 = df.loc[df["PARAM"] == "SpecifiedAnnualDemand"]
    df10
    Fuel_list10 = df10["FUEL"].tolist()
    Fuel_list10
    Year_list10 = df10["YEAR"].tolist()
    Year_list10d = []
    Counter10 = []
    Assignedcounter10 = []
    Assign10f = []

    for i in Year_list10:
        if i not in Year_list10d:
            Year_list10d.append(i)

    maxcounter10 =  len(Year_list10d)
    maxcounter10
    for j in range(0, len(Fuel_list177)):

        a10 = 0.001 + Value_list177[j]
        b10 = Fuel_list177[j]

        for y in Fuel_list10:
            Counterstring10 = str(y)
            if b10 in y and Assignedcounter10.count(Counterstring10) < maxcounter10:
                Assign10.append(a10)
                Assign10f.append(y)
                Assignedcounter10.append(Counterstring10)
                # print(Counterstring10)
            elif (b10 not in y) and (y not in Fuel_list177) and (Counter10.count(Counterstring10) < maxcounter10):
                Assign10.append(0)
                Assign10f.append(y)
                # print(Counterstring10)
            Counter10.append(Counterstring10)
    df10["Assignment"] = Assign10
    df10["Assignmentf"] = Assign10f
    sum_column = df10["Assignment"] + df10["VALUE"]
    df10["SUM"] = sum_column
    df10.drop("VALUE", axis=1, inplace=True)
    df10.drop("Assignment", axis=1, inplace=True)
    df10.drop("FUEL", axis=1, inplace=True)
    df10.rename(columns={"SUM": "VALUE"}, inplace=True)
    df10.rename(columns={"Assignmentf": "FUEL"}, inplace=True)
    df10 = df10[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "SpecifiedAnnualDemand"]
    df = df.reset_index(drop=True)
    df10 = df10.reset_index(drop=True)
    df = df.append(df10, ignore_index=True)
    df

    # SpecifiedDemandProfile
    import numpy as np

    # Profile preparation
    df499 = specified_demand_profile_cf
    df499.columns
    Fuel_list177 = df499.columns.tolist()
    Fuel_list177
    df11 = df.loc[df["PARAM"] == "SpecifiedDemandProfile"]
    Fuel_list11 = df11["FUEL"].tolist()
    Fuel_list11d = []
    Counter = []
    for j in Fuel_list11:
        if j not in Fuel_list11d:
            Fuel_list11d.append(j)
    Fuel_list11d
    TS_list11 = df11["TIMESLICE"].tolist()
    TS_list11d = []

    for j in TS_list11:
        if j not in TS_list11d:
            TS_list11d.append(j)

    Year_list11 = df11["YEAR"].tolist()
    Year_list11d = []

    for k in Year_list11:
        if k not in Year_list11d:
            Year_list11d.append(k)

    maxcounter11 = len(TS_list11d) * len(Year_list11d)
    maxcounter11
    Assign11 = []
    Assign11f = []
    Assign11t = []
    Assign11y = []
    for j in range(0, len(Fuel_list177)):
        df1 = pd.DataFrame(df499[str(Fuel_list177[j])])
        len(df1)
        assign8784 = df1[str(Fuel_list177[j])].tolist()
        length = 8784 - len(assign8784)

        for i in range(0, length):
            assign8784.append(0)

        df1 = pd.DataFrame()
        df1[str(Fuel_list177[j])] = assign8784
        assign = []
        Timeslice = len(sets_df["TIMESLICE"])
        split = Timeslice / 24
        Marker = 8785 / (split)
        assign99 = []

        for k in range(1, 8785):
            i = (k / Marker) + 1
            assign99.append(int(i))

        df1["Marker"] = assign99

        assign999 = []
        for l in range(1, 367):
            for i in range(1, 25):
                assign999.append(int(i))

        df1["HourMarker"] = assign999
        table = pd.pivot_table(
            df1,
            index=["HourMarker"],
            columns=["Marker"],
            values=[str(Fuel_list177[j])],
            aggfunc=np.sum,
        )

        table.columns = table.columns.droplevel(0)
        table.index.name = None

        cols = [table[col].squeeze() for col in table]
        cols = pd.concat(cols, ignore_index=True)


        b11 = Fuel_list177[j]

        for x in Fuel_list11d:
            for y in TS_list11d:
                for z in Year_list11d:
                    Counterstring = str(x)
                    if b11 in x:
                        Assign11.append(cols[(int(y)) - 1])
                        Assign11f.append(x)
                        Assign11t.append(y)
                        Assign11y.append(z)
                    elif (
                        (b11 not in x)
                        and (x not in Fuel_list177)
                        and Counter.count(Counterstring) < maxcounter11
                    ):
                        # print(str(str(x) + str(y)))
                        Assign11.append(0)
                        Assign11f.append(x)
                        Assign11t.append(y)
                        Assign11y.append(z)
                    Counter.append(Counterstring)

    Assign11
    len(Assign11)
    df11["Assignment"] = Assign11
    df11["Assignmentf"] = Assign11f
    df11["Assignmentt"] = Assign11t
    df11["Assignmenty"] = Assign11y
    sum_column = df11["Assignment"] + df11["VALUE"]
    df11["SUM"] = sum_column
    df11.drop("VALUE", axis=1, inplace=True)
    df11.drop("TIMESLICE", axis=1, inplace=True)
    df11.drop("YEAR", axis=1, inplace=True)
    df11.drop("FUEL", axis=1, inplace=True)
    df11.drop("Assignment", axis=1, inplace=True)
    df11.rename(columns={"SUM": "VALUE"}, inplace=True)
    df11.rename(columns={"Assignmentf": "FUEL"}, inplace=True)
    df11.rename(columns={"Assignmentt": "TIMESLICE"}, inplace=True)
    df11.rename(columns={"Assignmenty": "YEAR"}, inplace=True)
    df11 = df11[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df11 = df11.reset_index(drop=True)
    df11
    df = df.loc[df["PARAM"] != "SpecifiedDemandProfile"]
    df = df.reset_index(drop=True)
    df = df.append(df11, ignore_index=True)
    df

    # CapacityFactor
    import numpy as np
    import pandas as pd

    df500 = capacity_factor_cf
    Tech_list177 = df500.columns.tolist()
    Tech_list177

    # Profile prepearation

    df12 = df.loc[df["PARAM"] == "CapacityFactor"]

    Tech_list12 = df12["TECHNOLOGY"].tolist()
    Tech_list12d = []

    for i in Tech_list12:
        if i not in Tech_list12d:
            Tech_list12d.append(i)
    Tech_list12d
    TS_list12 = df12["TIMESLICE"].tolist()
    TS_list12d = []

    for l in TS_list12:
        if l not in TS_list12d:
            TS_list12d.append(l)

    Year_list12 = df12["YEAR"].tolist()
    Year_list12d = []

    for k in Year_list12:
        if k not in Year_list12d:
            Year_list12d.append(k)

    maxcounter12 = len(TS_list12d) * len(Year_list12d)
    maxcounter12
    Assign12 = []
    Assign12ts = []
    Assign12t = []
    Assign12y = []
    assign1 = []
    Counter = []

    for j in range(0, len(Tech_list177)):
        df2 = pd.DataFrame(df500[str(Tech_list177[j])])
        Timeslice1 = len(sets_df["TIMESLICE"])
        split1 = Timeslice1 / 24
        Marker1 = 8785 / (split1)
        assign8784 = df2[str(Tech_list177[j])].tolist()
        length = 8784 - len(assign8784)

        for i in range(0, length):
            assign8784.append(1)

        df2 = pd.DataFrame()
        df2[str(Tech_list177[j])] = assign8784
        assign991 = []

        for l in range(1, 8785):
            i = (l / Marker1) + 1
            assign991.append(int(i))

        df2["Marker"] = assign991
        assign9991 = []
        for k in range(1, 367):
            for i in range(1, 25):
                assign9991.append(int(i))

        df2["HourMarker"] = assign9991

        table1 = pd.pivot_table(
            df2,
            index=["HourMarker"],
            columns=["Marker"],
            values=[str(Tech_list177[j])],
            aggfunc=np.mean,
        )

        table1.columns = table1.columns.droplevel(0)
        table1.index.name = None

        cols1 = [table1[col].squeeze() for col in table1]
        cols1 = pd.concat(cols1, ignore_index=True)

        # Writing dataframe

        b12 = str(Tech_list177[j])
        a12 = -1

        for x in Tech_list12d:
            for y in TS_list12d:
                for z in Year_list12d:
                    Counterstring = str(x)
                    if b12 in x:
                        Assign12.append(cols1[(int(y)) - 1] + a12)
                        Assign12t.append(x)
                        Assign12ts.append(y)
                        Assign12y.append(z)
                    elif (
                        (b12 not in x)
                        and (x not in Tech_list177)
                        and Counter.count(Counterstring) < maxcounter12
                    ):
                        Assign12.append(0)
                        Assign12t.append(x)
                        Assign12ts.append(y)
                        Assign12y.append(z)
                    Counter.append(Counterstring)
    Assign12
    len(df12)
    df12["Assignment"] = Assign12
    df12["Assignmentt"] = Assign12t
    df12["Assignmentts"] = Assign12ts
    df12["Assignmenty"] = Assign12y
    sum_column = df12["Assignment"] + df12["VALUE"]
    df12["SUM"] = sum_column
    df12.drop("VALUE", axis=1, inplace=True)
    df12.drop("TIMESLICE", axis=1, inplace=True)
    df12.drop("TECHNOLOGY", axis=1, inplace=True)
    df12.drop("YEAR", axis=1, inplace=True)
    df12.drop("Assignment", axis=1, inplace=True)
    df12.rename(columns={"SUM": "VALUE"}, inplace=True)
    df12.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df12.rename(columns={"Assignmentts": "TIMESLICE"}, inplace=True)
    df12.rename(columns={"Assignmenty": "YEAR"}, inplace=True)
    df12 = df12[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df12 = df12.reset_index(drop=True)
    df12
    df = df.loc[df["PARAM"] != "CapacityFactor"]
    df = df.reset_index(drop=True)
    df = df.append(df12, ignore_index=True)
    df

    # PLATFORMAVAILABILITYFACTOR
    df472 = platform_technologies
    Tech_list173 = df472["technology"].tolist()
    Value_list173 = df472["availability_factor"].tolist()
    Assign13 = []
    Assign13t = []
    df13 = df.loc[df["PARAM"] == "AvailabilityFactor"]
    Tech_list13 = df13["TECHNOLOGY"].tolist()

    Year_list13 = df13["YEAR"].tolist()
    Year_list13d = []
    for i in Year_list13:
        if i not in Year_list13d:
            Year_list13d.append(i)

    counter13 = []
    maxcounter13 = len(Year_list13d)

    for j in range(0, len(Tech_list173)):

        a13 = Value_list173[j]
        Tech_list13
        b13 = Tech_list173[j]
        for y in Tech_list13:
            counterstring13 = str(y)
            if str(b13) in y and a13 != 0:
                Assign13.append((-1 + a13))
                Assign13t.append(y)
            elif str(b13) in y and a13 == 0:
                Assign13.append(a13)
                Assign13t.append(y)
            elif (b13 not in y) and (y not in Tech_list173) and (counter13.count(counterstring13) < maxcounter13):
                Assign13.append(0)
                Assign13t.append(y)
            counter13.append(counterstring13)

    df13["Assignment"] = Assign13
    df13["Assignmentt"] = Assign13t
    sum_column = df13["Assignment"] + df13["VALUE"]
    df13["SUM"] = sum_column
    df13.drop("VALUE", axis=1, inplace=True)
    df13.drop("TECHNOLOGY", axis=1, inplace=True)
    df13.drop("Assignment", axis=1, inplace=True)
    df13.rename(columns={"SUM": "VALUE"}, inplace=True)
    df13.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df13 = df13[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "AvailabilityFactor"]
    df = df.reset_index(drop=True)
    df13 = df13.reset_index(drop=True)
    df = df.append(df13, ignore_index=True)

    # PLATFORMCAPITALCOSTSTORAGE
    df475 = platform_storages
    Sto_list175 = df475["storage"].tolist()

    Value_list175 = df475["capital_cost_storage"].tolist()

    Assign14 = []
    Assign14s = []

    df14 = df.loc[df["PARAM"] == "CapitalCostStorage"]

    Sto_list14 = df14["STORAGE"].tolist()
    Sto_list14

    Year_list14 = df14["YEAR"].tolist()
    Year_list14d = []

    counter14 = []
    maxcounter14 = len(Year_list14d)
    for i in Year_list14:
        if i not in Year_list14d:
            Year_list14d.append(i)

    for j in range(0, len(Sto_list175)):

        a14 = Value_list175[j]

        b14 = Sto_list175[j]

        for y in Sto_list14:

            if b14 in y:
                counterstring14 = str(y)
                Assign14.append(a14)
                Assign14s.append(y)
            elif (b14 not in y) and (y not in Sto_list175) and (counter14.count(counterstring14) < maxcounter14):
                Assign14.append(0)
                Assign14s.append(y)
            counter14.append(counterstring14)

    len(Assign14)
    df14["Assignment"] = Assign14
    df14["Assignments"] = Assign14s
    sum_column = df14["Assignment"] + df14["VALUE"]
    df14["SUM"] = sum_column
    df14.drop("VALUE", axis=1, inplace=True)
    df14.drop("STORAGE", axis=1, inplace=True)
    df14.drop("Assignment", axis=1, inplace=True)
    df14.rename(columns={"SUM": "VALUE"}, inplace=True)
    df14.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df14 = df14[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "CapitalCostStorage"]
    df = df.reset_index(drop=True)
    df14 = df14.reset_index(drop=True)
    df = df.append(df14, ignore_index=True)
    df

    # PLATFORMDISCOUNTRATETECH
    df472 = platform_technologies
    Tech_list173 = df472["technology"].tolist()

    Value_list173 = df472["discount_rate_tech"].tolist()
    Assign15 = []
    Assign15t = []
    df15 = df.loc[df["PARAM"] == "DiscountRateTech"]

    Year_list15 = df15["YEAR"].tolist()
    Year_list15d = []

    for i in Year_list15:
        if i not in Year_list15d:
            Year_list15d.append(i)

    counter15 = []
    maxcounter15 = len(Year_list15d)
    for j in range(0, len(Tech_list173)):

        a15 = Value_list173[j]
        Tech_list15 = df15["TECHNOLOGY"].tolist()
        Tech_list15
        b15 = Tech_list173[j]

        Tech_list15 = df15["TECHNOLOGY"].tolist()

        for y in Tech_list15:
            counterstring15 = str(y)
            if str(b15) in y and (a15 == 0):
                Assign15.append(a15)
                Assign15t.append(y)
            elif str(b15) in y and (a15 != 0):
                Assign15.append(-0.04 + a15)
                Assign15t.append(y)
            elif (b15 not in y) and (y not in Tech_list173) and (counter15.count(counterstring15) < maxcounter15):
                Assign15.append(0)
                Assign15t.append(y)
            counter15.append(counterstring15)

    df15["Assignment"] = Assign15
    sum_column = df15["Assignment"] + df15["VALUE"]
    df15["SUM"] = sum_column
    df15.drop("VALUE", axis=1, inplace=True)
    df15.drop("Assignment", axis=1, inplace=True)
    df15.rename(columns={"SUM": "VALUE"}, inplace=True)
    df15 = df15[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "DiscountRateTech"]
    df = df.reset_index(drop=True)
    df15 = df15.reset_index(drop=True)
    df = df.append(df15, ignore_index=True)

    ##PLATFORMDISCOUNTRATESTO
    df468 = platform_storages
    Sto_list170 = df468["storage"].tolist()

    Value_list170 = df468["dicount_rate_sto"].tolist()

    Assign16 = []
    Assign16s = []
    df16 = df.loc[df["PARAM"] == "DiscountRateSto"]

    Sto_list16 = df16["STORAGE"].tolist()
    Sto_list16

    Year_list16 = df16["YEAR"].tolist()
    Year_list16d = []

    for i in Year_list16:
        if i not in Year_list16d:
            Year_list16d.append(i)

    counter16 = []
    maxcounter16 = len(Year_list16d)

    for j in range(0, len(Sto_list170)):

        a16 = Value_list170[j]

        b16 = Sto_list170[j]

        for y in Sto_list16:
            counterstring16 = str(y)
            if b16 in y and (a16 != 0):
                Assign16.append(-0.04 + a16)
                Assign16s.append(y)
            elif b16 in y and (a16 == 0):
                Assign16.append(a16)
                Assign16s.append(y)
            elif (b16 not in y) and (y not in Sto_list170) and (counter16.count(counterstring16) < maxcounter16):
                Assign16.append(0)
            counter16.append(counterstring16)

    df16["Assignment"] = Assign16
    df16["Assignments"] = Assign16s
    sum_column = df16["Assignment"] + df16["VALUE"]
    df16["SUM"] = sum_column
    df16.drop("VALUE", axis=1, inplace=True)
    df16.drop("Assignment", axis=1, inplace=True)
    df16.drop("STORAGE", axis=1, inplace=True)
    df16.rename(columns={"SUM": "VALUE"}, inplace=True)
    df16.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df16 = df16[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "DiscountRateSto"]
    df = df.reset_index(drop=True)
    df16 = df16.reset_index(drop=True)
    df = df.append(df16, ignore_index=True)

    # PLATFORMCAPACITYTOACTIVITYUNIT
    df471 = platform_technologies
    Tech_list113 = df471["technology"].tolist()

    Value_list113 = df471["capacity_to_activity"].tolist()
    Assign17 = []
    Assign17t = []
    df17 = df.loc[df["PARAM"] == "CapacityToActivityUnit"]

    Tech_list17 = df17["TECHNOLOGY"].tolist()
    Tech_list17d = []

    for i in Tech_list17:
        if i not in Tech_list17d:
            Tech_list17d.append(i)
    counter17 = []

    for j in range(0, len(Tech_list113)):

        a17 = Value_list113[j]
        Tech_list17 = df17["TECHNOLOGY"].tolist()
        Tech_list17
        b17 = Tech_list113[j]


        for y in Tech_list17d:
            counterstring17 = str(y)
            if b17 in y and (a17 != 0):
                Assign17.append(-8760 + a17)
                Assign17t.append(y)
            elif b17 in y and (a17 == 0):
                Assign17.append(a17)
                Assign17t.append(y)
            elif (b17 not in y) and (y not in Tech_list113) and (counter17.count(counterstring17) < 1):
                Assign17.append(0)
            counter17.append(counterstring17)

    df17["Assignment"] = Assign17
    df17["Assignmentt"] = Assign17t
    sum_column = df17["Assignment"] + df17["VALUE"]
    df17["SUM"] = sum_column
    df17.drop("VALUE", axis=1, inplace=True)
    df17.drop("TECHNOLOGY", axis=1, inplace=True)
    df17.drop("Assignment", axis=1, inplace=True)
    df17.rename(columns={"SUM": "VALUE"}, inplace=True)
    df17.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df17 = df17[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "CapacityToActivityUnit"]
    df = df.reset_index(drop=True)
    df17 = df17.reset_index(drop=True)
    df = df.append(df17, ignore_index=True)

    # PLATFORMANNUALEMISSIONLIMIT
    df469 = platform_annual_emission_limit
    EM_list170 = df469["emission"].tolist()
    EM_list170
    Value_list170 = df469["annual_emission_limit"].tolist()

    Assign18 = []
    Assign18e = []
    counter18 = []
    df18 = df.loc[df["PARAM"] == "AnnualEmissionLimit"]

    EM_list18 = df18["EMISSION"].tolist()

    Year_list18 = df18["YEAR"].tolist()
    Year_list18d = []

    for i in Year_list18:
        if i not in Year_list18d:
            Year_list18d.append(i)
    maxcounter18 = len(Year_list18d) 

    for j in range(0, len(EM_list170)):

        a18 = Value_list170[j]

        b18 = EM_list170[j]

        for y in EM_list18:
            counterstring18 = str(y)
            if b18 in y and (a18 != 0):
                Assign18.append(-99999999999 + a18)
                Assign18e.append(y)
            elif b18 in y and (a18 == 0):
                Assign18.append(a18)
                Assign18e.append(y)
            elif(b18 not in y) and (y not in EM_list170) and (counter18.count(counterstring18) < maxcounter18):
                Assign18.append(0)
                Assign18e.append(y)
            counter18.append(counterstring18)

    df18["Assignment"] = Assign18
    df18["Assignmente"] = Assign18e
    sum_column = df18["Assignment"] + df18["VALUE"]
    df18["SUM"] = sum_column
    df18.drop("VALUE", axis=1, inplace=True)
    df18.drop("EMISSION", axis=1, inplace=True)
    df18.drop("Assignment", axis=1, inplace=True)
    df18.rename(columns={"SUM": "VALUE"}, inplace=True)
    df18.rename(columns={"Assignmente": "EMISSION"}, inplace=True)
    df18 = df18[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "AnnualEmissionLimit"]
    df = df.reset_index(drop=True)
    df18 = df18.reset_index(drop=True)
    df = df.append(df18, ignore_index=True)
    df

    # PLATFORMOPERATIONALLIFESTO
    df468 = platform_storages
    Sto_list170 = df468["storage"].tolist()

    Value_list170 = df468["operational_life_sto"].tolist()

    Assign19 = []
    Assign19s = []
    counter19 = []
    df19 = df.loc[df["PARAM"] == "OperationalLifeStorage"]

    Sto_list19 = df19["STORAGE"].tolist()
    Sto_list19

    Year_list19 = df19["YEAR"].tolist()
    Year_list19d = []

    for i in Year_list19:
        if i not in Year_list19d:
            Year_list19d.append(i)

    for j in range(0, len(Sto_list170)):

        a19 = Value_list170[j]

        b19 = Sto_list170[j]

        for y in Sto_list19:
            counterstring19 = str(y)
            if b19 in y and (a19 != 0):
                Assign19.append(-99 + a19)
                Assign19s.append(y)
            elif b19 in y and (a19 == 0):
                Assign19.append(a19)
                Assign19s.append(y)
            elif (b19 not in y) and (y not in Sto_list170) and (counter19.count(counterstring19) < 1):
                Assign19.append(0)
                Assign19s.append(y)
            counter19.append(counterstring19)

    df19["Assignment"] = Assign19
    df19["Assignments"] = Assign19s
    sum_column = df19["Assignment"] + df19["VALUE"]
    df19["SUM"] = sum_column
    df19.drop("VALUE", axis=1, inplace=True)
    df19.drop("STORAGE", axis=1, inplace=True)
    df19.drop("Assignment", axis=1, inplace=True)
    df19.rename(columns={"SUM": "VALUE"}, inplace=True)
    df19.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df19 = df19[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "OperationalLifeStorage"]
    df = df.reset_index(drop=True)
    df19 = df19.reset_index(drop=True)
    df = df.append(df19, ignore_index=True)
    df

   # PLATFORMSTOMAXDISCHARGERATE
    df469 = platform_storages
    Sto_list129 = df469["storage"].tolist()

    Value_list129 = df469["storage_max_discharge"].tolist()

    Assign20 = []
    Assign20s = []
    counter20 = []
    df20 = df.loc[df["PARAM"] == "StorageMaxDischargeRate"]

    Sto_list20 = df20["STORAGE"].tolist()
    Sto_list20

    Year_list20 = df20["YEAR"].tolist()
    Year_list20d = []

    for i in Year_list20:
        if i not in Year_list20d:
            Year_list20d.append(i)
    maxcounter20 =len(Year_list20d)
    for j in range(0, len(Sto_list129)):

        a20 = Value_list129[j]

        b20 = Sto_list129[j]

        for y in Sto_list20:
            counterstring20 = str(y)
            if b20 in y and (a20 != 0):
                Assign20.append(-999999999 + a20)
                Assign20s.append(y)
            elif b20 in y and (a20 == 0):
                Assign20.append(a20)
                Assign20s.append(y)
            elif (b20 not in y) and (y not in Sto_list129) and (counter20.count(counterstring20) < maxcounter20):
                Assign20.append(0)
                Assign20s.append(y)
            counter20.append(counterstring20)

    df20["Assignment"] = Assign20
    df20["Assignments"] = Assign20s
    sum_column = df20["Assignment"] + df20["VALUE"]
    df20["SUM"] = sum_column
    df20.drop("VALUE", axis=1, inplace=True)
    df20.drop("STORAGE", axis=1, inplace=True)
    df20.drop("Assignment", axis=1, inplace=True)
    df20.rename(columns={"SUM": "VALUE"}, inplace=True)
    df20.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df20 = df20[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageMaxDischargeRate"]
    df = df.reset_index(drop=True)
    df20 = df20.reset_index(drop=True)
    df = df.append(df20, ignore_index=True)


    # PLATFORMSTOMAXCHARGERATE
    df467 = platform_storages
    Sto_list128 = df467["storage"].tolist()

    Value_list128 = df467["storage_max_charge"].tolist()

    Assign21 = []
    Assign21s = []
    counter21= []
    df21 = df.loc[df["PARAM"] == "StorageMaxChargeRate"]

    Sto_list21 = df21["STORAGE"].tolist()
    Sto_list21

    Year_list21 = df21["YEAR"].tolist()
    Year_list21d = []

    for i in Year_list21:
        if i not in Year_list21d:
            Year_list21d.append(i)

    maxcounter21 = len(Year_list21d)

    for j in range(0, len(Sto_list128)):

        a21 = Value_list128[j]

        b21 = Sto_list128[j]

        for y in Sto_list21:
            counterstring21 = str(y)
            if b21 in y and (a21 != 0):
                Assign21.append(-999999999 + a21)
                Assign21s.append(0)
            elif b21 in y and (a21 == 0):
                Assign21.append(a21)
                Assign21s.append(0)
            elif (b21 not in y) and (y not in Sto_list128) and (counter21.count(counterstring21) < maxcounter21):
                Assign21.append(0)
                Assign21s.append(0)
            counter21.append(counterstring21)

    df21["Assignment"] = Assign21
    df21["Assignments"] = Assign21s
    sum_column = df21["Assignment"] + df21["VALUE"]
    df21["SUM"] = sum_column
    df21.drop("VALUE", axis=1, inplace=True)
    df21.drop("STORAGE", axis=1, inplace=True)
    df21.drop("Assignment", axis=1, inplace=True)
    df21.rename(columns={"SUM": "VALUE"}, inplace=True)
    df21.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df21 = df21[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageMaxChargeRate"]
    df = df.reset_index(drop=True)
    df21 = df21.reset_index(drop=True)
    df = df.append(df21, ignore_index=True)
    df

    # PLATFORMStorageL2D
    df466 = platform_storages
    Sto_list127 = df466["storage"].tolist()

    Value_list127 = df466["l2d"].tolist()

    Assign22 = []
    Assign22s = []
    counter22 = []
    df22 = df.loc[df["PARAM"] == "StorageL2D"]

    Sto_list22 = df22["STORAGE"].tolist()
    Sto_list22

    Year_list22 = df22["YEAR"].tolist()
    Year_list22d = []

    for i in Year_list22:
        if i not in Year_list22d:
            Year_list22d.append(i)


    for j in range(0, len(Sto_list127)):

        a22 = Value_list127[j]

        b22 = Sto_list127[j]

        for y in Sto_list22:
            counterstring22 = str(y)
            if b22 in y:
                Assign22.append(a22)
                Assign22s.append(y)
            elif (b22 not in y) and (y not in Sto_list127) and (counter22.count(counterstring22) < 1):
                Assign22.append(0)
                Assign22s.append(y)
            counter22.append(counterstring22)

    df22["Assignment"] = Assign22
    df22["Assignments"] = Assign22s
    sum_column = df22["Assignment"] + df22["VALUE"]
    df22["SUM"] = sum_column
    df22.drop("VALUE", axis=1, inplace=True)
    df22.drop("STORAGE", axis=1, inplace=True)
    df22.drop("Assignment", axis=1, inplace=True)
    df22.rename(columns={"SUM": "VALUE"}, inplace=True)
    df22.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df22 = df22[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageL2D"]
    df = df.reset_index(drop=True)
    df22 = df22.reset_index(drop=True)
    df = df.append(df22, ignore_index=True)

    # PLATFORMStoragetagheating
    df465 = platform_storages
    Sto_list126 = df465["storage"].tolist()

    Value_list126 = df465["tag_heating"].tolist()

    Assign23 = []
    Assign23s = []
    counter23 = []
    df23 = df.loc[df["PARAM"] == "Storagetagheating"]

    Sto_list23 = df23["STORAGE"].tolist()
    Sto_list23

    Year_list23 = df23["YEAR"].tolist()
    Year_list23d = []

    for i in Year_list23:
        if i not in Year_list23d:
            Year_list23d.append(i)

    for j in range(0, len(Sto_list126)):

        a23 = Value_list126[j]

        b23 = Sto_list126[j]

        for y in Sto_list23:
            counterstring23 = str(y)
            if b23 in y:
                Assign23.append(a23)
                Assign23s.append(y)
            elif (b23 not in y) and (y not in Sto_list126) and (counter23.count(counterstring23) < 1):
                Assign23.append(0)
                Assign23s.append(y)
            counter23.append(counterstring23)

    df23["Assignment"] = Assign23
    df23["Assignments"] = Assign23s
    sum_column = df23["Assignment"] + df23["VALUE"]
    df23["SUM"] = sum_column
    df23.drop("VALUE", axis=1, inplace=True)
    df23.drop("STORAGE", axis=1, inplace=True)
    df23.drop("Assignment", axis=1, inplace=True)
    df23.rename(columns={"SUM": "VALUE"}, inplace=True)
    df23.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df23 = df23[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "Storagetagheating"]
    df = df.reset_index(drop=True)
    df23 = df23.reset_index(drop=True)
    df = df.append(df23, ignore_index=True)

    # PLATFORMStorageReturnTemperature
    df463 = platform_storages
    Sto_list124 = df463["storage"].tolist()

    Value_list124 = df463["storage_return_temp"].tolist()

    Assign25 = []
    Assign25s = []
    counter25 = []
    df25 = df.loc[df["PARAM"] == "StorageReturnTemperature"]

    Sto_list25 = df25["STORAGE"].tolist()
    Sto_list25

    Year_list25 = df25["YEAR"].tolist()
    Year_list25d = []

    for i in Year_list25:
        if i not in Year_list25d:
            Year_list25d.append(i)

    maxcounter25 = len(Year_list25d)

    for j in range(0, len(Sto_list124)):

        a25 = Value_list124[j]

        b25 = Sto_list124[j]

        for y in Sto_list25:
            counterstring25 = str(y)
            if b25 in y and a25 != 0:
                Assign25.append(-50 + a25)
                Assign25s.append(y)
            elif b25 in y and a25 == 0:
                Assign25.append(a25)
                Assign25s.append(y)
            elif (b25 not in y) and (y not in Sto_list124) and (counter25.count(counterstring25) < maxcounter25):
                Assign25.append(0)
                Assign25s.append(y)
            counter25.append(counterstring25)

    df25["Assignment"] = Assign25
    df25["Assignments"] = Assign25s
    sum_column = df25["Assignment"] + df25["VALUE"]
    df25["SUM"] = sum_column
    df25.drop("VALUE", axis=1, inplace=True)
    df25.drop("Assignment", axis=1, inplace=True)
    df25.drop("STORAGE", axis=1, inplace=True)
    df25.rename(columns={"SUM": "VALUE"}, inplace=True)
    df25.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df25 = df25[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageReturnTemperature"]
    df = df.reset_index(drop=True)
    df25 = df25.reset_index(drop=True)
    df = df.append(df25, ignore_index=True)

    # PLATFORMStorageFlowTemperature
    df462 = platform_storages
    Sto_list123 = df462["storage"].tolist()

    Value_list123 = df462["storage_supply_temp"].tolist()

    Assign26 = []
    Assign26s = []
    counter26 = []

    df26 = df.loc[df["PARAM"] == "StorageFlowTemperature"]

    Sto_list26 = df26["STORAGE"].tolist()
    Sto_list26

    Year_list26 = df26["YEAR"].tolist()
    Year_list26d = []

    for i in Year_list26:
        if i not in Year_list26d:
            Year_list26d.append(i)

    maxcounter = len(Year_list26d)

    for j in range(0, len(Sto_list123)):

        a26 = Value_list123[j]

        b26 = Sto_list123[j]

        for y in Sto_list26:
            counterstring26 = str(y)
            if b26 in y and a26 != 0:
                Assign26.append(-80 + a26)
                Assign26s.append(y)
            elif b26 in y and a26 == 0:
                Assign26.append(a26)
                Assign26s.append(y)
            elif (b26 not in y) and (y not in Sto_list123) and (counter26.count(counterstring26) < maxcounter26):
                Assign26.append(0)
                Assign26s.append(y)
            counter26.append(counterstring26)

    df26["Assignment"] = Assign26
    df26["Assignments"] = Assign26s
    sum_column = df26["Assignment"] + df26["VALUE"]
    df26["SUM"] = sum_column
    df26.drop("VALUE", axis=1, inplace=True)
    df26.drop("STORAGE", axis=1, inplace=True)
    df26.drop("Assignment", axis=1, inplace=True)
    df26.rename(columns={"SUM": "VALUE"}, inplace=True)
    df26.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df26 = df26[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageFlowTemperature"]
    df = df.reset_index(drop=True)
    df26 = df26.reset_index(drop=True)
    df = df.append(df26, ignore_index=True)


    # PLATFORMStorageAmbientTemperature
    df461 = platform_storages
    Sto_list122 = df461["storage"].tolist()

    Value_list122 = df461["storage_ambient_temp"].tolist()
    Value_list122
    Assign27 = []
    Assign27s = []
    counter27 = []
    df27 = df.loc[df["PARAM"] == "StorageAmbientTemperature"]

    Sto_list27 = df27["STORAGE"].tolist()
    Sto_list27

    Year_list27 = df27["YEAR"].tolist()
    Year_list27d = []

    for i in Year_list27:
        if i not in Year_list27d:
            Year_list27d.append(i)

    maxcounter27 = len(Year_list27d)

    for j in range(0, len(Sto_list122)):

        a27 = Value_list122[j]

        b27 = Sto_list122[j]

        for y in Sto_list27:
            counterstring27 = str(y)
            if b27 in y and a27 != 0:
                Assign27.append(-15 + a27)
                Assign27s.append(y)
            elif b27 in y and a27 == 0:
                Assign27.append(a27)
                Assign27s.append(y)
            elif (b27 not in y) and (y not in Sto_list27) and (counter27.count(counterstring27) < maxcounter27):
                Assign27.append(0)
                Assign27s.append(y)
            counter27.append(counterstring27)

    df27["Assignment"] = Assign27
    df27["Assignments"] = Assign27s
    sum_column = df27["Assignment"] + df27["VALUE"]
    df27["SUM"] = sum_column
    df27.drop("VALUE", axis=1, inplace=True)
    df27.drop("STORAGE", axis=1, inplace=True)
    df27.drop("Assignment", axis=1, inplace=True)
    df27.rename(columns={"SUM": "VALUE"}, inplace=True)
    df27.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df27 = df27[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageAmbientTemperature"]
    df = df.reset_index(drop=True)
    df27 = df27.reset_index(drop=True)
    df = df.append(df27, ignore_index=True)


    # PLATFORMResidualCapacity
    df460 = platform_technologies
    Tech_list121 = df460["technology"].tolist()

    Value_list121 = df460["residual_capacity"].tolist()
    Value_list121
    df28 = df.loc[df["PARAM"] == "ResidualCapacity"]
    Assign28 = []
    Assign28t = []
    counter28 = []
    Tech_list28 = df28["TECHNOLOGY"].tolist()
    Tech_list28

    Year_list28 = df28["YEAR"].tolist()
    Year_list28d = []

    for i in Year_list28:
        if i not in Year_list28d:
            Year_list28d.append(i)

    maxcounter28 =  len(Year_list28d)

    for j in range(0, len(Tech_list121)):

        a28 = Value_list121[j]

        b28 = Tech_list121[j]

        for y in Tech_list28:
            counterstring28 = str(y)
            if b28 in y:
                Assign28.append(a28)
                Assign28t.append(y)
            elif (b28 not in y) and (y not in Tech_list121) and (counter28.count(counterstring28) < maxcounter28):
                Assign28.append(0)
                Assign28t.append(y)
            counter28.append(counterstring28)

    df28["Assignment"] = Assign28
    df28["Assignmentt"] = Assign28t
    sum_column = df28["Assignment"] + df28["VALUE"]
    df28["SUM"] = sum_column
    df28.drop("VALUE", axis=1, inplace=True)
    df28.drop("TECHNOLOGY", axis=1, inplace=True)
    df28.drop("Assignment", axis=1, inplace=True)
    df28.rename(columns={"SUM": "VALUE"}, inplace=True)
    df28.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df28 = df28[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "ResidualCapacity"]
    df = df.reset_index(drop=True)
    df28 = df28.reset_index(drop=True)
    df = df.append(df28, ignore_index=True)

    # PLATFORMResidualStorageCapacity
    df459 = platform_storages
    Sto_list119 = df459["storage"].tolist()

    Value_list119 = df459["residual_storage_capacity"].tolist()
    Value_list119
    Assign29 = []
    Assign29s = []
    counter29 = []
    df29 = df.loc[df["PARAM"] == "ResidualStorageCapacity"]

    Sto_list29 = df29["STORAGE"].tolist()
    Sto_list29

    Year_list29 = df29["YEAR"].tolist()
    Year_list29d = []

    for i in Year_list29:
        if i not in Year_list29d:
            Year_list29d.append(i)

    maxcounter29 = len(Year_list29d)

    for j in range(0, len(Sto_list119)):

        a29 = Value_list119[j]

        b29 = Sto_list119[j]

        for y in Sto_list29:
            counterstring29 = str(y)
            if b29 in y:
                Assign29.append(a29)
                Assign29s.append(y)
            elif (b29 not in y) and (y not in Sto_list29) and (counter29.count(counterstring29) < maxcounter29):
                Assign29.append(0)
                Assign29s.append(y)
            counter29.append(counterstring29)

    df29["Assignment"] = Assign29
    df29["Assignments"] = Assign29s
    sum_column = df29["Assignment"] + df29["VALUE"]
    df29["SUM"] = sum_column
    df29.drop("VALUE", axis=1, inplace=True)
    df29.drop("STORAGE", axis=1, inplace=True)
    df29.drop("Assignment", axis=1, inplace=True)
    df29.rename(columns={"SUM": "VALUE"}, inplace=True)
    df29.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df29 = df29[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "ResidualStorageCapacity"]
    df = df.reset_index(drop=True)
    df29 = df29.reset_index(drop=True)
    df = df.append(df29, ignore_index=True)
    df

    # PLATFORMStorageMaxCapacity
    df458 = platform_storages
    Sto_list119 = df458["storage"].tolist()
    Value_list119 = df458["max_storage_capacity"].tolist()
    Assign30 = []
    Assign30s = []
    counter30 = []
    df30 = df.loc[df["PARAM"] == "StorageMaxCapacity"]
    Sto_list31 = df30["STORAGE"].tolist()
    Sto_list31d = []

    for i in Sto_list31:
        if i not in Sto_list31d:
            Sto_list31d.append(i)

    for j in range(0, len(Sto_list119)):

        a30 = Value_list119[j]

        b30 = Sto_list119[j]

        for y in Sto_list31d:
            counterstring30 = str(y)
            if b30 in y and a30 != 0:
                Assign30.append(-999999999 + a30)
                Assign30s.append(y)
            elif b30 in y and a30 == 0:
                Assign30.append(a30)
                Assign30s.append(y)
            elif (b30 not in y) and (y not in Sto_list119) and (counter30.count(counterstring30) < 1):
                Assign30.append(0)
                Assign30s.append(y)
            counter30.count(counterstring30) 

    df30["Assignment"] = Assign30
    df30["Assignments"] = Assign30s
    sum_column = df30["Assignment"] + df30["VALUE"]
    df30["SUM"] = sum_column
    df30.drop("VALUE", axis=1, inplace=True)
    df30.drop("STORAGE", axis=1, inplace=True)
    df30.drop("Assignment", axis=1, inplace=True)
    df30.rename(columns={"SUM": "VALUE"}, inplace=True)
    df30.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df30 = df30[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageMaxCapacity"]
    df = df.reset_index(drop=True)
    df30 = df30.reset_index(drop=True)
    df = df.append(df30, ignore_index=True)

    # PLATFORMStorageLevelStart
    df457 = platform_storages
    Sto_list118 = df457["storage"].tolist()
    Value_list118 = df457["storage_level_start"].tolist()
    Assign31 = []
    Assign31s = []
    counter31 = []
    df31 = df.loc[df["PARAM"] == "StorageLevelStart"]
    Sto_list31 = df31["STORAGE"].tolist()
    Sto_list31d = []

    for i in Sto_list31:
        if i not in Sto_list31d:
            Sto_list31d.append(i)

    for j in range(0, len(Sto_list118)):

        a31 = Value_list118[j]

        b31 = Sto_list118[j]

        for y in Sto_list31:
            counterstring31 = str(y)
            if b31 in y:
                Assign31.append(a31)
                Assign31s.append(y)
            elif (b31 not in y) and (y not in Sto_list118) and (counter31.count(counterstring31) < 1):
                Assign31.append(0)
                Assign31s.append(y)
            counter31.append(counterstring31)

    df31["Assignment"] = Assign31
    df31["Assignments"] = Assign31s
    sum_column = df31["Assignment"] + df31["VALUE"]
    df31["SUM"] = sum_column
    df31.drop("VALUE", axis=1, inplace=True)
    df31.drop("STORAGE", axis=1, inplace=True)
    df31.drop("Assignment", axis=1, inplace=True)
    df31.rename(columns={"SUM": "VALUE"}, inplace=True)
    df31.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df31 = df31[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageLevelStart"]
    df = df.reset_index(drop=True)
    df31 = df31.reset_index(drop=True)
    df = df.append(df31, ignore_index=True)
            
    # PLATFORMStorageUvalue
    df456 = platform_storages
    Sto_list117 = df456["storage"].tolist()

    Value_list117 = df456["u_value"].tolist()
    Value_list117
    Assign32 = []
    Assign32s = []
    counter32 = []

    df32 = df.loc[df["PARAM"] == "StorageUvalue"]

    Sto_list32 = df32["STORAGE"].tolist()
    Sto_list32

    Year_list32 = df32["YEAR"].tolist()
    Year_list32d = []

    for i in Year_list32:
        if i not in Year_list32d:
            Year_list32d.append(i)

    maxcounter32 = len(Year_list32d)

    for j in range(0, len(Sto_list117)):

        a32 = Value_list117[j]

        b32 = Sto_list117[j]

        for y in Sto_list32:
            counterstring32 = str(y)
            if b32 in y and a32 != 0:
                Assign32.append(-0.22 + a32)
                Assign32s.append(y)
            elif b32 in y and a32 == 0:
                Assign32.append(a32)
                Assign32s.append(y)
            elif (b32 not in y) and (y not in Sto_list32) and (counter32.count(counterstring32) < maxcounter32):
                Assign32.append(0)
                Assign32s.append(y)
            counter32.append(counterstring32)

    df32["Assignment"] = Assign32
    df32["Assignments"] = Assign32s
    sum_column = df32["Assignment"] + df32["VALUE"]
    df32["SUM"] = sum_column
    df32.drop("VALUE", axis=1, inplace=True)
    df32.drop("STORAGE", axis=1, inplace=True)
    df32.drop("Assignment", axis=1, inplace=True)
    df32.rename(columns={"SUM": "VALUE"}, inplace=True)
    df32.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df32 = df32[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "StorageUvalue"]
    df = df.reset_index(drop=True)
    df32 = df32.reset_index(drop=True)
    df = df.append(df32, ignore_index=True)

    # PLATFORMTechnologyFromStorage
    import itertools
    df485 = platform_technology_to_storage
    Tech_list113 = df485["technology"].tolist()
    Value_list113 = df485["technologyfromstorage"].tolist()
    Sto_list113 = df485["storage"].tolist()

    df33 = df.loc[df["PARAM"] == "TechnologyFromStorage"]
    df33

    Assign33 = []

    Tech_list33 = df33["TECHNOLOGY"].tolist()
    Tech_list33d = []

    for i in Tech_list33:
        if i not in Tech_list33d:
            Tech_list33d.append(i)

    Tech_list33d
    Sto_list33 = df33["STORAGE"].tolist()
    Sto_list33
    Sto_list33d = []

    for j in Sto_list33:
        if j not in Sto_list33d:
            Sto_list33d.append(j)

    MO_list33 = df33["MODE_OF_OPERATION"].tolist()
    MO_list33d = []

    for l in MO_list33:
        if l not in MO_list33d:
            MO_list33d.append(l)

    identifier33 = []

    for o in range(0, len(Tech_list113)):
        identifier33.append(str(Sto_list113[o] + Tech_list113[o]))

    identifier33
    Assign33m = []
    Assign33s = []
    Assign33t = []
    Counter33 = []
    maxcounter33 = len(MO_list33d)
    maxcounter33
    for k in range(0, len(Tech_list113)):
            a33 = Value_list113[k]
            b33 = Tech_list113[k]
            c33 = Sto_list113[k]
            for w in MO_list33d:
                for x in Sto_list33d:
                    for y in Tech_list33d:
                        Counterstring33 = str(str(x) + str(y))
                        if (b33) in y and (c33) in x and (int(w) == 1):
                            Assign33.append(a33)
                            Assign33m.append(w)
                            Assign33s.append(x)
                            Assign33t.append(y)
                        elif (((b33)in y) and ((c33) in x)) and (int(w) != 1):
                            Assign33.append(0)
                            Assign33m.append(w)
                            Assign33s.append(x)
                            Assign33t.append(y)                        
                        elif (((b33) not in y) or ((c33) not in x)) and (Counterstring33 not in identifier33) and (Counter33.count(Counterstring33) < maxcounter33):
                            Assign33.append(0)
                            Assign33m.append(w)
                            Assign33s.append(x)
                            Assign33t.append(y)
                        Counter33.append(Counterstring33)

    df33["Assignment"] = Assign33
    df33["Assignmentm"] = Assign33m
    df33["Assignmentt"] = Assign33t
    df33["Assignments"] = Assign33s
    df33
    sum_column = df33["Assignment"] + df33["VALUE"]
    df33["SUM"] = sum_column
    df33.drop("VALUE", axis=1, inplace=True)
    df33.drop("TECHNOLOGY", axis=1, inplace=True)
    df33.drop("MODE_OF_OPERATION", axis=1, inplace=True)
    df33.drop("STORAGE", axis=1, inplace=True)
    df33.drop("Assignment", axis=1, inplace=True)
    df33.rename(columns={"SUM": "VALUE"}, inplace=True)
    df33.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df33.rename(columns={"Assignmentm": "MODE_OF_OPERATION"}, inplace=True)
    df33.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df33 = df33[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df33
    df = df.loc[df["PARAM"] != "TechnologyFromStorage"]
    df = df.reset_index(drop=True)
    df33 = df33.reset_index(drop=True)
    df = df.append(df33, ignore_index=True)

    # PLATFORMTechnologyToStorage
    import itertools
    df484 = platform_technology_to_storage
    Tech_list112 = df484["technology"].tolist()
    Value_list112 = df484["technologytostorage"].tolist()
    Sto_list112 = df484["storage"].tolist()

    df34 = df.loc[df["PARAM"] == "TechnologyToStorage"]
    df34

    Assign34 = []

    Tech_list34 = df34["TECHNOLOGY"].tolist()
    Tech_list34d = []

    for i in Tech_list34:
        if i not in Tech_list34d:
            Tech_list34d.append(i)

    Tech_list34d
    Sto_list34 = df34["STORAGE"].tolist()
    Sto_list34
    Sto_list34d = []

    for j in Sto_list34:
        if j not in Sto_list34d:
            Sto_list34d.append(j)

    MO_list34 = df34["MODE_OF_OPERATION"].tolist()
    MO_list34d = []

    for l in MO_list34:
        if l not in MO_list34d:
            MO_list34d.append(l)

    identifier34 = []

    for o in range(0, len(Tech_list112)):
        identifier34.append(str(Sto_list112[o] + Tech_list112[o]))

    identifier34
    Assign34m = []
    Assign34s = []
    Assign34t = []
    Counter34 = []
    maxcounter34 = len(MO_list34d)
    maxcounter34
    for k in range(0, len(Tech_list112)):
            a34 = Value_list112[k]
            b34 = Tech_list112[k]
            c34 = Sto_list112[k]
            for w in MO_list34d:
                for x in Sto_list34d:
                    for y in Tech_list34d:
                        Counterstring34 = str(str(x) + str(y))
                        if (b34) in y and (c34) in x and (int(w) == 2):
                            #print(str(str(x) + str(y) + '1'))
                            Assign34.append(a34)
                            Assign34m.append(w)
                            Assign34s.append(x)
                            Assign34t.append(y)
                        elif (((b34)  in y) and ((c34) in x)) and (int(w) != 2):
                            Assign34.append(0)
                            Assign34m.append(w)
                            Assign34s.append(x)
                            Assign34t.append(y)
                        elif (((b34) not in y) or ((c34) not in x)) and (Counterstring34 not in identifier34) and (Counter34.count(Counterstring34) < maxcounter34):
                            #print(print(str(str(x) + str(y)+ '0')))
                            Assign34.append(0)
                            Assign34m.append(w)
                            Assign34s.append(x)
                            Assign34t.append(y)
                        Counter34.append(Counterstring34)

    df34["Assignment"] = Assign34
    df34["Assignmentm"] = Assign34m
    df34["Assignmentt"] = Assign34t
    df34["Assignments"] = Assign34s
    df34
    sum_column = df34["Assignment"] + df34["VALUE"]
    df34["SUM"] = sum_column
    df34.drop("VALUE", axis=1, inplace=True)
    df34.drop("TECHNOLOGY", axis=1, inplace=True)
    df34.drop("MODE_OF_OPERATION", axis=1, inplace=True)
    df34.drop("STORAGE", axis=1, inplace=True)
    df34.drop("Assignment", axis=1, inplace=True)
    df34.rename(columns={"SUM": "VALUE"}, inplace=True)
    df34.rename(columns={"Assignments": "STORAGE"}, inplace=True)
    df34.rename(columns={"Assignmentm": "MODE_OF_OPERATION"}, inplace=True)
    df34.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df34 = df34[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df34
    df = df.loc[df["PARAM"] != "TechnologyToStorage"]
    df = df.reset_index(drop=True)
    df34 = df34.reset_index(drop=True)
    df = df.append(df34, ignore_index=True)

    # PLATFORMTotalAnnualMaxCapacityInvestment
    df454 = platform_technologies
    Tech_list117 = df454["technology"].tolist()
    Tech_list117
    Value_list117 = df454["max_capacity_investment"].tolist()
    Assign35 = []
    Assign35t = []
    counter35 = []
    df35 = df.loc[df["PARAM"] == "TotalAnnualMaxCapacityInvestment"]

    Tech_list35 = df35["TECHNOLOGY"].tolist()
    Tech_list35

    Year_list35 = df35["YEAR"].tolist()
    Year_list35d = []

    for i in Year_list35:
        if i not in Year_list35d:
            Year_list35d.append(i)

    maxcounter35 = len(Year_list35d)

    for j in range(0, len(Tech_list117)):

        a35 = Value_list117[j]

        b35 = Tech_list117[j]

        for y in Tech_list35:
            counterstring35 = str(y)
            if b35 in y and a35 != 0:
                Assign35.append(-999999999 + a35)
                Assign35t.append(y)
            elif b35 in y and a35 == 0:
                Assign35.append(a35)
                Assign35t.append(y)
            elif (b35 not in y) and (y not in Tech_list35) and (counter35.count(counterstring35) < maxcounte35):
                Assign35.append(0)
                Assign35t.append(y)
            counter35.append(counterstring35)

    df35["Assignment"] = Assign35
    df35["Assignmentt"] = Assign35t
    sum_column = df35["Assignment"] + df35["VALUE"]
    df35["SUM"] = sum_column
    df35.drop("VALUE", axis=1, inplace=True)
    df35.drop("TECHNOLOGY", axis=1, inplace=True)
    df35.drop("Assignment", axis=1, inplace=True)
    df35.rename(columns={"SUM": "VALUE"}, inplace=True)
    df35.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df35 = df35[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "TotalAnnualMaxCapacityInvestment"]
    df = df.reset_index(drop=True)
    df35 = df35.reset_index(drop=True)
    df = df.append(df35, ignore_index=True)

    # PLATFORMTotalAnnualMinCapacity
    df420 = platform_technologies
    Tech_list116 = df420["technology"].tolist()
    Tech_list116
    Value_list116 = df420["min_capacity"].tolist()
    Assign36 = []
    Assign36t = []
    counter36 = []
    df36 = df.loc[df["PARAM"] == "TotalAnnualMinCapacity"]

    Tech_list36 = df36["TECHNOLOGY"].tolist()
    Tech_list36

    Year_list36 = df36["YEAR"].tolist()
    Year_list36d = []

    for i in Year_list36:
        if i not in Year_list36d:
            Year_list36d.append(i)

    maxcounter36 = len(Year_list36d)
    for j in range(0, len(Tech_list116)):

        a36 = Value_list116[j]

        b36 = Tech_list116[j]

        for y in Tech_list36:
            counterstring36 = str(y)
            if str(b36) in y:
                Assign36.append(a36)
                Assign36t.append(y)
            elif (b36 not in y) and (y not in Tech_list36) and (counter36.count(counterstring36) < maxcounter36):
                Assign36.append(0)
                Assign36t.append(y)
            counter36.append(counterstring36)

    df36["Assignment"] = Assign36
    df36["Assignmentt"] = Assign36t
    sum_column = df36["Assignment"] + df36["VALUE"]
    df36["SUM"] = sum_column
    df36.drop("VALUE", axis=1, inplace=True)
    df36.drop("TECHNOLOGY", axis=1, inplace=True)
    df36.drop("Assignment", axis=1, inplace=True)
    df36.rename(columns={"SUM": "VALUE"}, inplace=True)
    df36.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df36 = df36[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "TotalAnnualMinCapacity"]
    df = df.reset_index(drop=True)
    df36 = df36.reset_index(drop=True)
    df = df.append(df36, ignore_index=True)

    # PLATFORMTotalAnnualMinCapacityInvestment
    df466 = platform_technologies
    Tech_list115 = df466["technology"].tolist()
    Tech_list115
    Value_list115 = df466["min_capacity_investment"].tolist()
    Assign37 = []
    Assign37t = []
    counter37 = []
    df37 = df.loc[df["PARAM"] == "TotalAnnualMinCapacityInvestment"]

    Tech_list37 = df37["TECHNOLOGY"].tolist()
    Tech_list37

    Year_list37 = df37["YEAR"].tolist()
    Year_list37d = []

    for i in Year_list37:
        if i not in Year_list37d:
            Year_list37d.append(i)

    maxcounter37 = len(Year_list37d)  

    for j in range(0, len(Tech_list115)):

        a37 = Value_list115[j]

        b37 = Tech_list115[j]

        for y in Tech_list37:
            counterstring37 = str(y)
            if str(b37) in y:
                Assign37.append(a37)
                Assign37t.append(y)
            elif (b37 not in y) and (y not in Tech_list115) and (counter37.count(counterstring37) < maxcounter37):
                Assign37.append(0)
                Assign37t.append(y)
            counter37.append(counterstring37)

    df37["Assignment"] = Assign37
    df37["Assignmentt"] = Assign37t
    sum_column = df37["Assignment"] + df37["VALUE"]
    df37["SUM"] = sum_column
    df37.drop("VALUE", axis=1, inplace=True)
    df37.drop("TECHNOLOGY", axis=1, inplace=True)
    df37.drop("Assignment", axis=1, inplace=True)
    df37.rename(columns={"SUM": "VALUE"}, inplace=True)
    df37.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df37 = df37[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "TotalAnnualMinCapacityInvestment"]
    df = df.reset_index(drop=True)
    df37 = df37.reset_index(drop=True)
    df = df.append(df37, ignore_index=True)


    # PLATFORMTotalTechnologyAnnualActivityLowerLimit
    df478 = platform_technologies
    Tech_list115 = df478["technology"].tolist()

    Value_list115 = df478["annual_activity_lower_limit"].tolist()
    Assign38 = []
    Assign38t = []
    counter38 = []
    df38 = df.loc[df["PARAM"] == "TotalTechnologyAnnualActivityLowerLimit"]

    Tech_list38 = df38["TECHNOLOGY"].tolist()
    Tech_list38

    Year_list38 = df38["YEAR"].tolist()
    Year_list38d = []

    for i in Year_list38:
        if i not in Year_list38d:
            Year_list38d.append(i)

    maxcounter38 = len(Year_list38d) 

    for j in range(0, len(Tech_list115)):

        a38 = Value_list115[j]

        b38 = Tech_list115[j]

        for y in Tech_list38:
            counterstring38 = str(y)
            if str(b38) in y:
                Assign38.append(a38)
                Assign38t.append(y)
            elif (b38 not in y) and (y not in Tech_list115) and (counter38.count(counterstring38) < maxcounter38):
                Assign38.append(0)
                Assign38t.append(y)
            counter38.append(counterstring38)

    df38["Assignment"] = Assign38
    df38["Assignmentt"] = Assign38t
    sum_column = df38["Assignment"] + df38["VALUE"]
    df38["SUM"] = sum_column
    df38.drop("VALUE", axis=1, inplace=True)
    df38.drop("TECHNOLOGY", axis=1, inplace=True)
    df38.drop("Assignment", axis=1, inplace=True)
    df38.rename(columns={"SUM": "VALUE"}, inplace=True)
    df38.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df38 = df38[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "TotalTechnologyAnnualActivityLowerLimit"]
    df = df.reset_index(drop=True)
    df38 = df38.reset_index(drop=True)
    df = df.append(df38, ignore_index=True)

    # PLATFORMTotalTotalTechnologyAnnualActivityUpperLimit
    df471 = platform_technologies
    Tech_list114 = df471["technology"].tolist()

    Value_list114 = df471["annual_activity_upper_limit"].tolist()

    Assign39 = []
    Assign39t = []
    counter39 = []
    df39 = df.loc[df["PARAM"] == "TotalTechnologyAnnualActivityUpperLimit"]


    Tech_list39 = df39["TECHNOLOGY"].tolist()
    Tech_list39

    Year_list39 = df39["YEAR"].tolist()
    Year_list39d = []

    for i in Year_list39:
        if i not in Year_list39d:
            Year_list39d.append(i)

    maxcounter39 = len(Year_list39d)

    for j in range(0, len(Tech_list114)):

        a39 =  Value_list114[j]

        b39 = Tech_list114[j]

        for y in Tech_list39:
            counterstring39 = str(y)
            if b39 in y and a39 != 0:
                Assign39.append(-9999999999 + a39)
                Assign39t.append(y)
            elif b39 in y and a39 == 0:
                Assign39.append(a39)
                Assign39t.append(y)
            elif (b39 not in y) and (y not in Tech_list114) and (counter39.count(counterstring39) < maxcounter39):
                Assign39.append(0)
                Assign39t.append(y)
            counter39.append(counterstring39)

    df39["Assignment"] = Assign39
    df39["Assignmentt"] = Assign39t
    sum_column = df39["Assignment"] + df39["VALUE"]
    df39["SUM"] = sum_column
    df39.drop("VALUE", axis=1, inplace=True)
    df39.drop("TECHNOLOGY", axis=1, inplace=True)
    df39.drop("Assignment", axis=1, inplace=True)
    df39.rename(columns={"SUM": "VALUE"}, inplace=True)
    df39.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df39 = df39[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "TotalTechnologyAnnualActivityUpperLimit"]
    df = df.reset_index(drop=True)
    df39 = df39.reset_index(drop=True)
    df = df.append(df39, ignore_index=True)

    # PLATFORMTotalTotalTechnologyModelPeriodActivityLowerLimit
    df405 = platform_technologies
    Tech_list113 = df405["technology"].tolist()
    Value_list113 = df405["model_period_activity_lower_limit"].tolist()

    Assign40 = []
    Assign40t = []
    counter40 = []
    df40 = df.loc[df["PARAM"] == "TotalTechnologyModelPeriodActivityLowerLimit"]
    Tech_list40 = df40["TECHNOLOGY"].tolist()
    Tech_list40d = []
    for i in Tech_list40:
        if i not in Tech_list40d:
            Tech_list40d.append(i)

    for j in range(0, len(Tech_list113)):

        a40 = Value_list113[j]
        b40 = Tech_list113[j]

        for y in Tech_list40:
            counterstring40 = str(y)
            if str(b40) in y:
                Assign40.append(a40)
                Assign40t.append(y)
            elif (b40 not in y) and (y not in Tech_list113) and (counter40.count(counterstring40) < maxcounter40):
                Assign40.append(0)
                Assign40t.append(y)
            counter40.count(counterstring40)

    df40["Assignment"] = Assign40
    df40["Assignmentt"] = Assign40t
    sum_column = df40["Assignment"] + df40["VALUE"]
    df40["SUM"] = sum_column
    df40.drop("VALUE", axis=1, inplace=True)
    df40.drop("TECHNOLOGY", axis=1, inplace=True)
    df40.drop("Assignment", axis=1, inplace=True)
    df40.rename(columns={"SUM": "VALUE"}, inplace=True)
    df40.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df40 = df40[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "TotalTechnologyModelPeriodActivityLowerLimit"]
    df = df.reset_index(drop=True)
    df40 = df40.reset_index(drop=True)
    df = df.append(df40, ignore_index=True)

    # PLATFORMTotalTotalTechnologyModelPeriodActivityUpperLimit
    df429 = platform_technologies
    Tech_list111 = df429["technology"].tolist()
    Tech_list111
    Value_list111 = df429["model_period_activity_upper_limit"].tolist()
    Assign41 = []
    Assign41t = []
    counter41 = []
    assignedcounter41 = []
    df41 = df.loc[df["PARAM"] == "TotalTechnologyModelPeriodActivityUpperLimit"]
    Tech_list41 = df41["TECHNOLOGY"].tolist()
    Tech_list41d = []

    for i in Tech_list41:
        if i not in Tech_list41d:
            Tech_list41d.append(i)

    for j in range(0, len(Tech_list111)):

        a41 = Value_list111[j]

        b41 = Tech_list111[j]

        for y in Tech_list41:
            counterstring41 = str(y)
            if b41 in y and a41 != 0 and (assignedcounter41.count(counterstring41) < 1):
                Assign41.append(-9999999999 + a41)
                Assign41t.append(y)
                assignedcounter41.append(counterstring41)
            elif b41 in y and a41 == 0 and (assignedcounter41.count(counterstring41) < 1):
                Assign41.append(a41)
                Assign41t.append(y)
                assignedcounter41.append(counterstring41)
            elif (b41 not in y) and (y not in Tech_list111) and (counter41.count(counterstring41) < 1):
                Assign41.append(0)
                Assign41t.append(y)
            counter41.append(counterstring41)

    df41["Assignment"] = Assign41
    df41["Assignmentt"] = Assign41t
    sum_column = df41["Assignment"] + df41["VALUE"]
    df41["SUM"] = sum_column
    df41.drop("VALUE", axis=1, inplace=True)
    df41.drop("TECHNOLOGY", axis=1, inplace=True)
    df41.drop("Assignment", axis=1, inplace=True)
    df41.rename(columns={"SUM": "VALUE"}, inplace=True)
    df41.rename(columns={"Assignmentt": "TECHNOLOGY"}, inplace=True)
    df41 = df41[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df = df.loc[df["PARAM"] != "TotalTechnologyModelPeriodActivityUpperLimit"]
    df = df.reset_index(drop=True)
    df41 = df41.reset_index(drop=True)
    df = df.append(df41, ignore_index=True)

    # PLATFORMYearSplit
    import numpy as np

    df41 = df.loc[df["PARAM"] == "YearSplit"]
    Timeslice = len(sets_df["TIMESLICE"])
    a41 = 1 / Timeslice

    TS_list41 = df41["TIMESLICE"].tolist()
    TS_list41d = []

    for j in TS_list41:
        if j not in TS_list41d:
            TS_list41d.append(j)

    Year_list41 = df41["YEAR"].tolist()
    Year_list41d = []

    for k in Year_list41:
        if k not in Year_list41d:
            Year_list41d.append(k)

    Assign41 = []

    for y in TS_list41d:
        for z in Year_list41d:
            Assign41.append(a41)

    Assign41
    len(df41)
    df41["Assignment"] = Assign41
    sum_column = df41["Assignment"] + df41["VALUE"]
    df41["SUM"] = sum_column
    df41.drop("VALUE", axis=1, inplace=True)
    df41.drop("Assignment", axis=1, inplace=True)
    df41.rename(columns={"SUM": "VALUE"}, inplace=True)
    df41 = df41[
        [
            "PARAM",
            "VALUE",
            "REGION",
            "REGION2",
            "DAYTYPE",
            "EMISSION",
            "FUEL",
            "DAILYTIMEBRACKET",
            "SEASON",
            "TIMESLICE",
            "STORAGE",
            "MODE_OF_OPERATION",
            "TECHNOLOGY",
            "YEAR",
        ]
    ]
    df41[df41["FUEL"] == str("SINK1DEMAND")]
    df = df.loc[df["PARAM"] != "YearSplit"]
    df = df.reset_index(drop=True)
    df = df.append(df41, ignore_index=True)

    return df
