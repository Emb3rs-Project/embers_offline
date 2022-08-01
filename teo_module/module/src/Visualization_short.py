import numpy as np
import plotly.express as px  
import numpy as np
import plotly.offline as pyo
import warnings
warnings.filterwarnings("ignore")
from flask import Markup, render_template
import plotly
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape
import pandas as pd
import re
import os
def Reportshort(Results, sets_df):
    
    #creating source, sink and stream IDs
    reslist = []
    for i in sets_df['TECHNOLOGY']['TECHNOLOGY']:
        res = re.findall('(\d+|[A-Za-z]+)', i)
        reslist.append(res)

    streamidlist = []
    sourcesinkidlist = []
    for i in range(0,len(reslist)):
        k = reslist[i]
        if len(k) > 1 and k[0] != 'str':
            streamidlist.append(k[3])
            sourcesinkidlist.append(k[1])
    streamidlistd = []
    sourcesinkidlistd = []

    for i in streamidlist:
        if int(i) not in streamidlistd:
            streamidlistd.append(int(i))

    for i in sourcesinkidlist:
        if int(i) not in sourcesinkidlistd:
            sourcesinkidlistd.append(int(i))

    # Start Visualization
    a = Results
    #Accumulated New Capacity
    AccumulatedNewCapacity = pd.DataFrame(a['AccumulatedNewCapacity'])
    AccumulatedNewCapacity
    Tech_list1 = AccumulatedNewCapacity['TECHNOLOGY'].tolist()
    Assign1 = []
    Assign2 = []
    Assign4 = []
    for x in Tech_list1:
        if("grid") in x:
            Assign1.append("Grid Specific")
            Assign4.append('')
        elif ("dhn") in x:
            Assign1.append("District Heating Network")
            Assign4.append('')
        else:
            10
            for i in sourcesinkidlistd:
                if (','.join(["sou%dstr" % i ])) in x:
                    Assign1.append(','.join(["Source%d" % i ]))            
                elif (','.join(["sink%dstr" % i ])) in x:
                    Assign1.append(','.join(["Sink%d" % i ]))
            if "sou" or "sink" in x:
                for i in streamidlistd:
                    if(','.join(["str%d" % i ])) in x:
                        Assign4.append(','.join(["Stream%d" % i ]))
            else:
                Assign4.append('')
            for i in streamidlistd:
                if(','.join(["str%dsou" % i ])) in x:
                    Assign1.append(','.join(["Stream%d" % i ])) 

        if ("gridspecificngboiler") in x:
            Assign2.append("Grid Specific Natural gas Boiler")
        elif ("gridspecificoilboiler") in x:
            Assign2.append("Grid Specific Oil Boiler")
        elif ("gridspecificbioboiler") in x:
            Assign2.append("Grid Specific Biomass Boiler")
        elif ("gridspecifichp") in x:
            Assign2.append("Grid Specific Heat Pump")
        elif ("gridspecificsthp") in x:
            Assign2.append("Grid Specific solar thermal with Heat Pump")
        elif ("dhn") in x:
            Assign2.append("District Heating Network")
        elif ("she") in x:
            Assign2.append("Single Heat Exchanger")      
        elif ("mhe") in x:
            Assign2.append("Multiple Heat Exchanger")
        elif ("elwhrb") in x:
            Assign2.append("Electric Waste Heat Recovery Boiler")
        elif ("ngwhrb") in x:
            Assign2.append("Natural Gas Heat Recovery Boiler")
        elif ("oilwhrb") in x:
            Assign2.append("Oil Heat Recovery Boiler")
        elif ("biomasswhrb") in x:
            Assign2.append("Biomass Heat Recovery Boiler")
        elif ("chpng") in x:
            Assign2.append("Natural Gas CHP")
        elif ("chpoil") in x:
            Assign2.append("Oil CHP")
        elif ("chpbiomass") in x:
            Assign2.append("Biomass CHP")
        elif ("boosthp") in x:
            Assign2.append("Booster Heat Pump")
        elif ("sthp") in x:
            Assign2.append("Solar thermal Heat Pump")
        elif ("stngboiler") in x:
            Assign2.append("Solar thermal with Natural gas boiler")
        elif ("stoilboiler") in x:
            Assign2.append("Solar thermal with oil boiler")
        elif ("stbiomassboiler") in x:
            Assign2.append("Solar thermal with biomass boiler")
        elif ("stelboiler") in x:
            Assign2.append("Solar thermal with el boiler")
        elif x.endswith('ac') is True:
            Assign2.append("Absorption Chiller")
        elif x.endswith('acec') is True:
            Assign2.append("Absorption Chiller with Electric Chiller")
        elif ("acngboiler") in x:
            Assign2.append("Absorption Chiller with Natural gas boiler")
        elif ("acoilboiler") in x:
            Assign2.append("Absorption Chiller with oil boiler")
        elif ("acbiomassboiler") in x:
            Assign2.append("Absorption Chiller with biomass boiler")
        elif ("acelectricboiler") in x:
            Assign2.append("Absorption Chiller with electric boiler")  
        elif ("acecngboiler") in x:
            Assign2.append("Absorption Chiller and Electric Chiller with Natural gas boiler")
        elif ("acecoilboiler") in x:
            Assign2.append("Absorption Chiller and Electric Chiller with oil boiler")
        elif ("acecbiomassboiler") in x:
            Assign2.append("Absorption Chiller and Electric Chiller with biomass boiler")
        elif ("acecelectricboiler") in x:
            Assign2.append("Absorption Chiller and Electric Chiller with electric boiler")
        elif ("acechp") in x:
            Assign2.append("Absorption Chiller and Electric Chiller with heat pump")
        elif ("achp") in x:
            Assign2.append("Absorption Chiller with heat pump")
        elif ("orc") in x:
            Assign2.append("Organic Rankine Cycle")
        elif ("exgrid") in x:
            Assign2.append("Existing Grid Technologies")
        elif("hp") in x:
            for i in streamidlistd:
                if(','.join(["str%dhp" % i ])) in x:
                    Assign2.append("Heat Pump") 
        else:
            Assign2.append(" ")

    Assign3 = []
    for i in range(0, len(Assign1)):
        if Assign1[i] in Assign2[i]:
            Assign3.append(Assign2[i])
        elif Assign2[i] == '':
            Assign3.append(str(str(Assign1[i]) + str(Assign2[i])))
        elif Assign4[i] in Assign1[i]:
            Assign3.append(str(str(Assign1[i] + ' ' + str(Assign2[i]))))
        elif Assign4[i] not in Assign1[i]:
            Assign3.append(str(str(Assign1[i] + ' ' + Assign4[i] + '' + str(Assign2[i]))))
    # print(Assign1)
    # print(Assign2)
    # print(Assign3)
    # print(Assign4)
    AccumulatedNewCapacity['Assignment'] = Assign3
    AccumulatedNewCapacity = AccumulatedNewCapacity.drop(['TECHNOLOGY'], axis = 1)
    AccumulatedNewCapacity = AccumulatedNewCapacity.drop(['NAME'], axis = 1)
    AccumulatedNewCapacity.rename(columns={"Assignment": "TECHNOLOGY"}, inplace=True)
    AccumulatedNewCapacity = AccumulatedNewCapacity[['VALUE', 'TECHNOLOGY', 'YEAR']]
    AccumulatedNewCapacityplot = AccumulatedNewCapacity.pivot_table(AccumulatedNewCapacity,index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
    AccumulatedNewCapacityplot = AccumulatedNewCapacityplot.reset_index()
    # del AccumulatedNewCapacityplot['index']
    AccumulatedNewCapacityplot = AccumulatedNewCapacityplot.droplevel(level=0, axis=1)
    list1 = AccumulatedNewCapacityplot.columns.tolist()
    list1.remove('')

    fig = px.bar(AccumulatedNewCapacityplot, x='', y=list1)
    fig.update_layout(
        title="Accumulated New Capacity",
        title_x=0.45,
        xaxis_title="Year",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Capaciy in kW",
        legend_title="Technologies",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )


    #source wise graph creation

    Techlist = AccumulatedNewCapacity["TECHNOLOGY"].tolist()
    Assign4 = []
    for x in Techlist:
        if "Source" in x:
            Assign4.append("Source")
        else:
            Assign4.append('')

    AccumulatedNewCapacity['Classification'] = Assign4
    Classlist = AccumulatedNewCapacity["Classification"].tolist()
    AccumulatedNewCapacitySource = AccumulatedNewCapacity.loc[AccumulatedNewCapacity["Classification"] == "Source"]
    del AccumulatedNewCapacitySource['Classification']
    Techlist = AccumulatedNewCapacitySource["TECHNOLOGY"].tolist()

    Assign5 = []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if str((','.join(["Source%d " % i ]))) in x:
                    Assign5.append(','.join(["Source%d" % i ]))
    AccumulatedNewCapacitySource['Classification'] = Assign5

    sourcelist = []
    for x in Techlist:
        for i in sourcesinkidlistd:
            if (','.join(["Source%d " % i ])) in x:
                sourcelist.append(','.join(["Source%d" % i ]))

    sourcelistd = []

    for i in sourcelist:
        if i not in sourcelistd:
            sourcelistd.append(i)
    ancsou = []    
    for i in sourcesinkidlistd:
        if (','.join(["Source%d" % i ])) in sourcelistd:
            df = AccumulatedNewCapacitySource.loc[AccumulatedNewCapacitySource["Classification"] == (','.join(["Source%d" % i ]))]
            dfplot = df.pivot_table(df,index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
            dfplot = dfplot.reset_index()
            dfplot = dfplot.droplevel(level=0, axis=1)
            list2 = dfplot.columns.tolist()
            list2.remove('')
            fig2 = px.bar(dfplot, x='', y=list2)
            fig2.update_layout(
                title=(','.join(["Accumulated New Capacity for Source %d" % i ])),
                title_x=0.45,
                xaxis_title="Year",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Capaciy in kW",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )

            ancsouel = plotly.io.to_html(fig2, full_html=False,include_plotlyjs=False)
            ancsou.append(ancsouel)

    # Sink wise graphs
    del AccumulatedNewCapacitySource['Classification']
    Techlist = AccumulatedNewCapacity["TECHNOLOGY"].tolist()
    Assign6 = []
    for x in Techlist:
        if "Sink" in x:
            Assign6.append("Sink")
        else:
            Assign6.append('')
    AccumulatedNewCapacity['Classification'] = Assign6
    Classlist = AccumulatedNewCapacity["Classification"].tolist()

    AccumulatedNewCapacitySink = AccumulatedNewCapacity.loc[AccumulatedNewCapacity["Classification"] == "Sink"]
    del AccumulatedNewCapacitySink['Classification']
    Techlist = AccumulatedNewCapacitySink["TECHNOLOGY"].tolist()

    Assign7 = []
    for x in Techlist:
        for i in sourcesinkidlistd:
            if str((','.join(["Sink%d " % i ]))) in x:
                Assign7.append(','.join(["Sink%d" % i ]))

    Techlist
    AccumulatedNewCapacitySink['Classification'] = Assign7

    sinklist = []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if (','.join(["Sink%d " % i ])) in x:
                sinklist.append(','.join(["Sink%d" % i ]))

    sinklistd =[]   

    for i in sinklist:
        if i not in sinklistd:
            sinklistd.append(i)

    ancsi = []          
    for i in sourcesinkidlistd:
        if (','.join(["Sink%d" % i ])) in sinklistd:
            df = AccumulatedNewCapacitySink.loc[AccumulatedNewCapacitySink["Classification"] == (','.join(["Sink%d" % i ]))]
            dfplot1 = df.pivot_table(df,index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
            dfplot1 = dfplot1.reset_index()
            dfplot1 = dfplot1.droplevel(level=0, axis=1)
            list3 = dfplot1.columns.tolist()
            list3.remove('')
            fig3= px.bar(dfplot1, x='', y=list3)
            fig3.update_layout(
                title=(','.join(["Accumulated New Capacity for Sink %d" % i ])),
                title_x=0.45,
                xaxis_title="Year",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Capaciy in kW",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )
            ancsiuel = plotly.io.to_html(fig3, full_html=False,include_plotlyjs=False)
            ancsi.append(ancsiuel)

    # Grid Specific
    Techlist = AccumulatedNewCapacity["TECHNOLOGY"].tolist()
    Assign8 = []
    for x in Techlist:
        if "Grid" in x:
            Assign8.append("Grid Specific")
        else:
            Assign8.append('')

    if "Grid Specific" in Assign8:
        AccumulatedNewCapacity['Classification'] = Assign8
        AccumulatedNewCapacityGrid = AccumulatedNewCapacity.loc[AccumulatedNewCapacity["Classification"] == "Grid Specific"]
        AccumulatedNewCapacityGridplot = AccumulatedNewCapacityGrid.pivot_table(AccumulatedNewCapacityGrid,index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
        AccumulatedNewCapacityGridplot = AccumulatedNewCapacityGridplot.reset_index()
        AccumulatedNewCapacityGridplot = AccumulatedNewCapacityGridplot.droplevel(level=0, axis=1)
        list4 = AccumulatedNewCapacityGridplot.columns.tolist()
        list4.remove('')
        fig4 = px.bar(AccumulatedNewCapacityGridplot, x='', y=list4)
        fig4.update_layout(
            title=("Accumulated New Capacity for Grid Specific Technologies"),
            title_x=0.45,
            xaxis_title="Year",
            paper_bgcolor='#FFFFFF',
            yaxis_title="Capaciy in kW",
            legend_title="Technologies",
            font=dict(
                family="Times New Roman",
                size=12,
                color="Black"
            )
        )


    #AccumulatedNewStorageCapacity
    AccumulatedNewStorageCapacity = pd.DataFrame(a['AccumulatedNewStorageCapacity'])

    AccumulatedNewStorageCapacityplot = AccumulatedNewStorageCapacity.pivot_table(AccumulatedNewStorageCapacity,index=['YEAR'],columns=['STORAGE'],aggfunc=np.sum)
    AccumulatedNewStorageCapacityplot = AccumulatedNewStorageCapacityplot.reset_index()
    AccumulatedNewStorageCapacityplot = AccumulatedNewStorageCapacityplot.droplevel(level=0, axis=1)
    liststo = AccumulatedNewStorageCapacityplot.columns.tolist()
    liststo.remove('')

    
    figsto = px.bar(AccumulatedNewStorageCapacityplot, x='', y=liststo)
    figsto.update_layout(
        title="Accumulated New Storage Capacity",
        title_x=0.45,
        xaxis_title="Year",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Storage Capacity in kWh",
        legend_title="Storage",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )



    #AnnualTechnologyEmission all combined, sink and source specific

    #AnnualTechnologyEmission all combined

    AnnualTechnologyEmission = pd.DataFrame(a['AnnualTechnologyEmission'])

    Tech_listem = AnnualTechnologyEmission['TECHNOLOGY'].tolist()
    Assignem1 = []
    Assignem2 = []
    Assignem4 = []                
    for x in Tech_listem:
        if("grid") in x:
            Assignem1.append("Grid Specific")
            Assignem4.append('')
        elif ("dhn") in x:
            Assignem1.append("District Heating Network")
            Assignem4.append('')
        else:
            for i in sourcesinkidlistd:
                if (','.join(["sou%dstr" % i ])) in x:
                    Assignem1.append(','.join(["Source%d" % i ]))
                elif (','.join(["sink%dstr" % i ])) in x:
                    Assignem1.append(','.join(["Sink%d" % i ]))
            if "sou" or "sink" in x:
                for i in streamidlistd:
                    if(','.join(["str%d" % i ])) in x:
                        Assignem4.append(','.join(["Stream%d" % i ]))
            else:
                Assignem4.append('')
            
            for i in streamidlistd:
                if(','.join(["str%dsou" % i ])) in x:
                    Assignem1.append(','.join(["Stream%d" % i ])) 

        if ("gridspecificngboiler") in x:
            Assignem2.append("Grid Specific Natural gas Boiler")
        elif ("gridspecificoilboiler") in x:
            Assignem2.append("Grid Specific Oil Boiler")
        elif ("gridspecificbioboiler") in x:
            Assignem2.append("Grid Specific Biomass Boiler")
        elif ("gridspecifichp") in x:
            Assignem2.append("Grid Specific Heat Pump")
        elif ("gridspecificsthp") in x:
            Assignem2.append("Grid Specific solar thermal with Heat Pump")
        elif ("dhn") in x:
            Assignem2.append("District Heating Network")
        elif ("she") in x:
            Assignem2.append("Single Heat Exchanger")      
        elif ("mhe") in x:
            Assignem2.append("Multiple Heat Exchanger")
        elif ("elwhrb") in x:
            Assignem2.append("Electric Waste Heat Recovery Boiler")
        elif ("ngwhrb") in x:
            Assignem2.append("Natural Gas Heat Recovery Boiler")
        elif ("oilwhrb") in x:
            Assignem2.append("Oil Heat Recovery Boiler")
        elif ("biomasswhrb") in x:
            Assignem2.append("Biomass Heat Recovery Boiler")
        elif ("chpng") in x:
            Assignem2.append("Natural Gas CHP")
        elif ("chpoil") in x:
            Assignem2.append("Oil CHP")
        elif ("chpbiomass") in x:
            Assignem2.append("Biomass CHP")
        elif ("hp") in x:
            Assignem2.append("Heat Pump")
        elif ("boosthp") in x:
            Assignem2.append("Booster Heat Pump")
        elif ("sthp") in x:
            Assignem2.append("Solar thermal Heat Pump")
        elif ("stngboiler") in x:
            Assignem2.append("Solar thermal with Natural gas boiler")
        elif ("stoilboiler") in x:
            Assignem2.append("Solar thermal with oil boiler")
        elif ("stbiomassboiler") in x:
            Assignem2.append("Solar thermal with biomass boiler")
        elif ("stelboiler") in x:
            Assignem2.append("Solar thermal with el boiler")
        elif x.endswith('ac') is True:
            Assignem2.append("Absorption Chiller")
        elif x.endswith('acec') is True:
            Assignem2.append("Absorption Chiller with Electric Chiller")
        elif ("acngboiler") in x:
            Assignem2.append("Absorption Chiller with Natural gas boiler")
        elif ("acoilboiler") in x:
            Assignem2.append("Absorption Chiller with oil boiler")
        elif ("acbiomassboiler") in x:
            Assignem2.append("Absorption Chiller with biomass boiler")
        elif ("acelectricboiler") in x:
            Assignem2.append("Absorption Chiller with electric boiler")  
        elif ("acecngboiler") in x:
            Assignem2.append("Absorption Chiller and Electric Chiller with Natural gas boiler")
        elif ("acecoilboiler") in x:
            Assignem2.append("Absorption Chiller and Electric Chiller with oil boiler")
        elif ("acecbiomassboiler") in x:
            Assignem2.append("Absorption Chiller and Electric Chiller with biomass boiler")
        elif ("acecelectricboiler") in x:
            Assignem2.append("Absorption Chiller and Electric Chiller with electric boiler")
        elif ("acechp") in x:
            Assignem2.append("Absorption Chiller and Electric Chiller with heat pump")
        elif ("achp") in x:
            Assignem2.append("Absorption Chiller with heat pump")
        elif ("orc") in x:
            Assignem2.append("Organic Rankine Cycle")
        elif ("exgrid") in x:
            Assignem2.append("Existing Grid Technologies")        
        
        elif("hp") in x:
            for i in streamidlistd:
                if(','.join(["str%dhp" % i ])) in x:
                    Assignem2.append("Heat Pump") 
        else:
            Assignem2.append(" ")

    Assignem3= []

    for i in range(0, len(Assignem1)):
        if Assignem1[i] in Assignem2[i]:
            Assignem3.append(Assignem2[i])
        elif Assignem2[i] == '':
            Assignem3.append(str(str(Assignem1[i]) + str(Assignem2[i])))
        else:
            Assignem3.append(str(str(Assignem1[i]) + ' ' + str(Assignem4[i])+ ' ' + str(Assignem2[i])))
    Assignem3

    AnnualTechnologyEmission['Assignment'] = Assignem3
    AnnualTechnologyEmission = AnnualTechnologyEmission.drop(['TECHNOLOGY'], axis = 1)
    AnnualTechnologyEmission = AnnualTechnologyEmission.drop(['NAME'], axis = 1)
    AnnualTechnologyEmission.rename(columns={"Assignment": "TECHNOLOGY"}, inplace=True)
    AnnualTechnologyEmission = AnnualTechnologyEmission[['VALUE', 'TECHNOLOGY', 'YEAR']]
    AnnualTechnologyEmission
    AnnualTechnologyEmissionplot = AnnualTechnologyEmission.pivot_table(AnnualTechnologyEmission,index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
    AnnualTechnologyEmissionplot = AnnualTechnologyEmissionplot.reset_index()
    AnnualTechnologyEmissionplot = AnnualTechnologyEmissionplot.droplevel(level=0, axis=1)
    listem = AnnualTechnologyEmissionplot.columns.tolist()
    listem.remove('')

    figem = px.bar(AnnualTechnologyEmissionplot, x='', y=listem)
    figem.update_layout(
        title="Annual Technology Emissions",
        title_x=0.45,
        xaxis_title="Year",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Emissions in Kg Co2eq",
        legend_title="Technologies",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )



    # source wise emissions graph creation

    Techlist = AnnualTechnologyEmission["TECHNOLOGY"].tolist()
    Techlist
    Assignem4 = []
    for x in Techlist:
        if "Source" in x:
            Assignem4.append("Source")
        else:
            Assignem4.append('')

    AnnualTechnologyEmission['Classification'] = Assignem4
    Classlist = AnnualTechnologyEmission["Classification"].tolist()
    Classlist
    AnnualTechnologyEmissionSource = AnnualTechnologyEmission.loc[AnnualTechnologyEmission["Classification"] == "Source"]
    del AnnualTechnologyEmissionSource['Classification']
    Techlist = AnnualTechnologyEmissionSource["TECHNOLOGY"].tolist()

    Assignem5 = []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if str((','.join(["Source%d " % i ]))) in x:
                    Assignem5.append(','.join(["Source%d" % i ]))

    AnnualTechnologyEmissionSource['Classification'] = Assignem5

    sourcelist = []
    for x in Techlist:
        for i in sourcesinkidlistd:
            if (','.join(["Source%d " % i ])) in x:
                sourcelist.append(','.join(["Source%d" % i ]))

    sourcelistd = []

    for i in sourcelist:
        if i not in sourcelistd:
            sourcelistd.append(i)

    emso = []
    for i in sourcesinkidlistd:
        if (','.join(["Source%d" % i ])) in sourcelistd:
            df = AnnualTechnologyEmissionSource.loc[AnnualTechnologyEmissionSource["Classification"] == (','.join(["Source%d" % i ]))]
            dfplot = df.pivot_table(df,index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
            dfplot = dfplot.reset_index()
            dfplot = dfplot.droplevel(level=0, axis=1)
            listem2 = dfplot.columns.tolist()
            listem2.remove('')
            figsoem = px.bar(dfplot, x='', y=listem2)
            figsoem.update_layout(
                title=(','.join(["Annual Technology Emissions for Source %d" % i ])),
                title_x=0.45,
                xaxis_title="Year",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Emissions in Kg Co2eq",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )
            emsouel = plotly.io.to_html(figsoem, full_html=False,include_plotlyjs=False)
            emso.append(emsouel)
    # Sink wise emission graphs

    Techlist = AnnualTechnologyEmission["TECHNOLOGY"].tolist()
    Assign6em= []
    for x in Techlist:
        if "Sink" in x:
            Assign6em.append("Sink")
        else:
            Assign6em.append('')
    AnnualTechnologyEmission['Classification'] = Assign6em
    Classlist = AnnualTechnologyEmission["Classification"].tolist()

    AnnualTechnologyEmissionSink = AnnualTechnologyEmission.loc[AnnualTechnologyEmission["Classification"] == "Sink"]
    del AnnualTechnologyEmissionSink['Classification']
    Techlist = AnnualTechnologyEmissionSink["TECHNOLOGY"].tolist()

    Assign7em= []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if str((','.join(["Sink%d " % i ]))) in x:
                    Assign7em.append(','.join(["Sink%d" % i ]))

    AnnualTechnologyEmissionSink['Classification'] = Assign7em

    sinklist = []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if (','.join(["Sink%d " % i ])) in x:
                sinklist.append(','.join(["Sink%d" % i ]))

    sinklistd =[]   

    for i in sinklist:
        if i not in sinklistd:
            sinklistd.append(i)

    emsi = []
    for i in sourcesinkidlistd:
        if (','.join(["Sink%d" % i ])) in sinklistd:
            df = AnnualTechnologyEmissionSink.loc[AnnualTechnologyEmissionSink["Classification"] == (','.join(["Sink%d" % i ]))]
            dfplot1 = df.pivot_table(df,index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
            dfplot1 = dfplot1.reset_index()
            dfplot1 = dfplot1.droplevel(level=0, axis=1)
            list3siem = dfplot1.columns.tolist()
            list3siem.remove('')
            fig3siem= px.bar(dfplot1, x='', y=list3siem)
            fig3siem.update_layout(
                title=(','.join(["Annual Technology Emissions for for Sink %d" % i ])),
                title_x=0.45,
                xaxis_title="Year",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Emissions in Kg Co2eq",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )
            emsiuel = plotly.io.to_html(fig3siem, full_html=False,include_plotlyjs=False)
            emsi.append(emsiuel)        

    # Grid Specific Emissions
    AnnualTechnologyEmission
    Techlist = AnnualTechnologyEmission["TECHNOLOGY"].tolist()
    Assign8em = []
    for x in Techlist:
        if "Grid" in x:
            Assign8em.append("Grid Specific")
        else:
            Assign8em.append('')
    if "Grid Specific" in Assign8em:
        AnnualTechnologyEmission['Classification'] = Assign8em
        AnnualTechnologyEmissionGrid = AnnualTechnologyEmission.loc[AnnualTechnologyEmission["Classification"] == "Grid Specific"]
        AnnualTechnologyEmissionGridplot = AnnualTechnologyEmissionGrid.pivot_table(AnnualTechnologyEmissionGrid,index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
        AnnualTechnologyEmissionGridplot = AnnualTechnologyEmissionGridplot.reset_index()
        AnnualTechnologyEmissionGridplot = AnnualTechnologyEmissionGridplot.droplevel(level=0, axis=1)
        list4 = AnnualTechnologyEmissionGridplot.columns.tolist()
        list4.remove('')
        figemgrid= px.bar(AnnualTechnologyEmissionGridplot, x='', y=list4)
        figemgrid.update_layout(
            title=("Accumulated New Capacity for Grid Specific Technologies"),
            title_x=0.45,
            xaxis_title="Year",
            paper_bgcolor='#FFFFFF',
            yaxis_title="Capaciy in kW",
            legend_title="Technologies",
            font=dict(
                family="Times New Roman",
                size=12,
                color="Black"
            )
        )

    # Capital Investment combined, source and sink

    # Capital Investment
    CapitalInvestment = pd.DataFrame(a['DiscountedCapitalInvestmentByTechnology'])
    CapitalInvestment 

    Tech_listem = CapitalInvestment['TECHNOLOGY'].tolist()
    AssignCI1 = []
    AssignCI2= []
    AssignCI4= []              
    for x in Tech_listem:
        if("grid") in x:
            AssignCI1.append("Grid Specific")
            AssignCI4.append('')
        elif ("dhn") in x:
            AssignCI1.append("District Heating Network")
            AssignCI4.append('')                           
        else:
            for i in sourcesinkidlistd:
                if (','.join(["sou%dstr" % i ])) in x:
                    AssignCI1.append(','.join(["Source%d" % i ]))
                elif (','.join(["sink%dstr" % i ])) in x:
                    AssignCI1.append(','.join(["Sink%d" % i ]))
            if "sou" or "sink" in x:
                for i in streamidlistd:
                    if(','.join(["str%d" % i ])) in x:
                        AssignCI4.append(','.join(["Stream%d" % i ]))
            else:
                AssignCI4.append('')
            for i in streamidlistd:
                if(','.join(["str%dsou" % i ])) in x:
                    AssignCI1.append(','.join(["Stream%d" % i ])) 


        if ("gridspecificngboiler") in x:
            AssignCI2.append("Grid Specific Natural gas Boiler")
        elif ("gridspecificoilboiler") in x:
            AssignCI2.append("Grid Specific Oil Boiler")
        elif ("gridspecificbioboiler") in x:
            AssignCI2.append("Grid Specific Biomass Boiler")
        elif ("gridspecifichp") in x:
            AssignCI2.append("Grid Specific Heat Pump")
        elif ("gridspecificsthp") in x:
            AssignCI2.append("Grid Specific solar thermal with Heat Pump")
        elif ("dhn") in x:
            AssignCI2.append("District Heating Network")
        elif ("she") in x:
            AssignCI2.append("Single Heat Exchanger")      
        elif ("mhe") in x:
            AssignCI2.append("Multiple Heat Exchanger")
        elif ("elwhrb") in x:
            AssignCI2.append("Electric Waste Heat Recovery Boiler")
        elif ("ngwhrb") in x:
            AssignCI2.append("Natural Gas Heat Recovery Boiler")
        elif ("oilwhrb") in x:
            AssignCI2.append("Oil Heat Recovery Boiler")
        elif ("biomasswhrb") in x:
            AssignCI2.append("Biomass Heat Recovery Boiler")
        elif ("chpng") in x:
            AssignCI2.append("Natural Gas CHP")
        elif ("chpoil") in x:
            AssignCI2.append("Oil CHP")
        elif ("chpbiomass") in x:
            AssignCI2.append("Biomass CHP")
        elif ("hp") in x:
            AssignCI2.append("Heat Pump")
        elif ("boosthp") in x:
            AssignCI2.append("Booster Heat Pump")
        elif ("sthp") in x:
            AssignCI2.append("Solar thermal Heat Pump")
        elif ("stngboiler") in x:
            AssignCI2.append("Solar thermal with Natural gas boiler")
        elif ("stoilboiler") in x:
            AssignCI2.append("Solar thermal with oil boiler")
        elif ("stbiomassboiler") in x:
            AssignCI2.append("Solar thermal with biomass boiler")
        elif ("stelboiler") in x:
            AssignCI2.append("Solar thermal with el boiler")
        elif x.endswith('ac') is True:
            AssignCI2.append("Absorption Chiller")
        elif x.endswith('acec') is True:
            AssignCI2.append("Absorption Chiller with Electric Chiller")
        elif ("acngboiler") in x:
            AssignCI2.append("Absorption Chiller with Natural gas boiler")
        elif ("acoilboiler") in x:
            AssignCI2.append("Absorption Chiller with oil boiler")
        elif ("acbiomassboiler") in x:
            AssignCI2.append("Absorption Chiller with biomass boiler")
        elif ("acelectricboiler") in x:
            AssignCI2.append("Absorption Chiller with electric boiler")  
        elif ("acecngboiler") in x:
            AssignCI2.append("Absorption Chiller and Electric Chiller with Natural gas boiler")
        elif ("acecoilboiler") in x:
            AssignCI2.append("Absorption Chiller and Electric Chiller with oil boiler")
        elif ("acecbiomassboiler") in x:
            AssignCI2.append("Absorption Chiller and Electric Chiller with biomass boiler")
        elif ("acecelectricboiler") in x:
            AssignCI2.append("Absorption Chiller and Electric Chiller with electric boiler")
        elif ("acechp") in x:
            AssignCI2.append("Absorption Chiller and Electric Chiller with heat pump")
        elif ("achp") in x:
            AssignCI2.append("Absorption Chiller with heat pump")
        elif ("orc") in x:
            AssignCI2.append("Organic Rankine Cycle")
        elif ("exgrid") in x:
            AssignCI2.append("Existing Grid Technologies")
        elif("hp") in x:
            for i in streamidlistd:
                if(','.join(["str%dhp" % i ])) in x:
                    AssignCI2.append("Heat Pump") 
        else:
            AssignCI2.append(" ")

    AssignCI3= []

    for i in range(0, len(AssignCI1)):
        if AssignCI1[i] in AssignCI2[i]:
            AssignCI3.append(AssignCI2[i])
        elif AssignCI2[i] == '':
            AssignCI3.append(str(str(AssignCI1[i]) + str(AssignCI2[i])))
        else:
            AssignCI3.append(str(str(AssignCI1[i]) + ' ' + str(AssignCI4[i])+ ' ' + str(AssignCI2[i])))
    AssignCI3

    CapitalInvestment['Assignment'] = AssignCI3
    CapitalInvestment = CapitalInvestment.drop(['TECHNOLOGY'], axis = 1)
    CapitalInvestment = CapitalInvestment.drop(['NAME'], axis = 1)
    CapitalInvestment.rename(columns={"Assignment": "TECHNOLOGY"}, inplace=True)
    CapitalInvestment = CapitalInvestment [['VALUE', 'TECHNOLOGY']]

    CapitalInvestment = CapitalInvestment.loc[CapitalInvestment["VALUE"] != 0] 

    figCI = px.bar(CapitalInvestment,x='TECHNOLOGY', y= 'VALUE')
    figCI.update_layout(
        title="Total Capital Investment",
        title_x=0.45,
        xaxis_title="Technologies",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Capital Investment in €",
        legend_title="Technologies",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )



    # source wise Capital Investment graph creation

    Techlist = CapitalInvestment["TECHNOLOGY"].tolist()
    Techlist
    AssignCI4 = []
    for x in Techlist:
        if "Source" in x:
            AssignCI4.append("Source")
        else:
            AssignCI4.append('')

    CapitalInvestment['Classification'] = AssignCI4
    Classlist = CapitalInvestment["Classification"].tolist()
    Classlist
    CapitalInvestmentSource = CapitalInvestment.loc[CapitalInvestment["Classification"] == "Source"]
    del CapitalInvestmentSource['Classification']
    Techlist = CapitalInvestmentSource["TECHNOLOGY"].tolist()
    AssignCI5 = []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if str((','.join(["Source%d " % i ]))) in x:
                    AssignCI5.append(','.join(["Source%d" % i ]))

    CapitalInvestmentSource['Classification'] = AssignCI5

    sourcelist = []
    for x in Techlist:
        for i in sourcesinkidlistd:
            if (','.join(["Source%d " % i ])) in x:
                sourcelist.append(','.join(["Source%d" % i ]))

    sourcelistd = []

    for i in sourcelist:
        if i not in sourcelistd:
            sourcelistd.append(i)
    ciso = []   
    for i in sourcesinkidlistd:
        if (','.join(["Source%d" % i ])) in sourcelistd:
            df = CapitalInvestmentSource.loc[CapitalInvestmentSource["Classification"] == (','.join(["Source%d" % i ]))]
            figsoCI = px.bar(df,x='TECHNOLOGY', y= 'VALUE')
            figsoCI.update_layout(
                title=(','.join(["Total Capital Investment for Source %d" % i ])),
                title_x=0.45,
                xaxis_title="Technologies",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Capital Investment in €",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )

            cisouel = plotly.io.to_html(figsoCI, full_html=False,include_plotlyjs=False)
            ciso.append(cisouel)    
    # Sink wise graphs
    Techlist = CapitalInvestment["TECHNOLOGY"].tolist()
    Assign6CIsi= []
    for x in Techlist:
        if "Sink" in x:
            Assign6CIsi.append("Sink")
        else:
            Assign6CIsi.append('')
    CapitalInvestment['Classification'] = Assign6CIsi
    Classlist = CapitalInvestment["Classification"].tolist()

    CapitalInvestmentSink = CapitalInvestment.loc[CapitalInvestment["Classification"] == "Sink"]
    del CapitalInvestmentSink['Classification']
    Techlist = CapitalInvestmentSink["TECHNOLOGY"].tolist()

    Assign7CIsi= []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if str((','.join(["Sink%d " % i ]))) in x:
                    Assign7CIsi.append(','.join(["Sink%d" % i ]))

    CapitalInvestmentSink['Classification'] = Assign7CIsi

    sinklist = []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if (','.join(["Sink%d " % i ])) in x:
                sinklist.append(','.join(["Sink%d" % i ]))

    sinklistd =[]   

    for i in sinklist:
        if i not in sinklistd:
            sinklistd.append(i)

    cisi = []

    for i in sourcesinkidlistd:
        if (','.join(["Sink%d" % i ])) in sinklistd:
            df = CapitalInvestmentSink.loc[CapitalInvestmentSink["Classification"] == (','.join(["Sink%d" % i ]))]
            fig3siCI= px.bar(df, x='TECHNOLOGY', y= 'VALUE')
            fig3siCI.update_layout(
                title=(','.join(["Total Capital Investment for Sink %d" % i ])),
                title_x=0.45,
                xaxis_title="Technologies",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Capital Investment in €",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )
            cisiuel = plotly.io.to_html(fig3siCI, full_html=False,include_plotlyjs=False)
            cisi.append(cisiuel) 

    # capital investment storage
    CapitalInvestmentsto = pd.DataFrame(a['DiscountedCapitalInvestmentByStorage'])
    CapitalInvestmentsto = CapitalInvestmentsto.loc[CapitalInvestmentsto["VALUE"] != 0] 
    del CapitalInvestmentsto['NAME']

    figCIS = px.bar(CapitalInvestmentsto,x='STORAGE', y= 'VALUE')
    figCIS.update_layout(
        title="Total Capital Investment Storage",
        title_x=0.45,
        xaxis_title="Storage",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Capital Investment Storage in €",
        legend_title="Storage",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )


    # Total Operating Cost - Combined, source and sink specific

    # Combined

    OperatingCost = pd.DataFrame(a['TotalDiscountedFixedOperatingCost'])
    OperatingCost = OperatingCost.loc[OperatingCost["VALUE"] >= 0.001] 

    Tech_listem = OperatingCost['TECHNOLOGY'].tolist()
    AssignOC1 = []
    AssignOC2= []
    AssignOC4= []  
    for x in Tech_listem:
        if("grid") in x:
            AssignOC1.append("Grid Specific")
            AssignOC4.append('')
        elif ("dhn") in x:
            AssignOC1.append("District Heating Network")
            AssignOC4.append('')
        else:
            for i in sourcesinkidlistd:
                if (','.join(["sou%dstr" % i ])) in x:
                    AssignOC1.append(','.join(["Source%d" % i ]))
                elif (','.join(["sink%dstr" % i ])) in x:
                    AssignOC1.append(','.join(["Sink%d" % i ]))
            if "sou" or "sink" in x:
                for i in streamidlistd:
                    if(','.join(["str%d" % i ])) in x:
                        AssignOC4.append(','.join(["Stream%d" % i ]))
            else:
                AssignOC4.append('')

            for i in streamidlistd:
                if(','.join(["str%dsou" % i ])) in x:
                    AssignOC1.append(','.join(["Stream%d" % i ])) 

        if ("gridspecificngboiler") in x:
            AssignOC2.append("Grid Specific Natural gas Boiler")
        elif ("gridspecificoilboiler") in x:
            AssignOC2.append("Grid Specific Oil Boiler")
        elif ("gridspecificbioboiler") in x:
            AssignOC2.append("Grid Specific Biomass Boiler")
        elif ("gridspecifichp") in x:
            AssignOC2.append("Grid Specific Heat Pump")
        elif ("gridspecificsthp") in x:
            AssignOC2.append("Grid Specific solar thermal with Heat Pump")
        elif ("dhn") in x:
            AssignOC2.append("District Heating Network")
        elif ("she") in x:
            AssignOC2.append("Single Heat Exchanger")      
        elif ("mhe") in x:
            AssignOC2.append("Multiple Heat Exchanger")
        elif ("elwhrb") in x:
            AssignOC2.append("Electric Waste Heat Recovery Boiler")
        elif ("ngwhrb") in x:
            AssignOC2.append("Natural Gas Heat Recovery Boiler")
        elif ("oilwhrb") in x:
            AssignOC2.append("Oil Heat Recovery Boiler")
        elif ("biomasswhrb") in x:
            AssignOC2.append("Biomass Heat Recovery Boiler")
        elif ("chpng") in x:
            AssignOC2.append("Natural Gas CHP")
        elif ("chpoil") in x:
            AssignOC2.append("Oil CHP")
        elif ("chpbiomass") in x:
            AssignOC2.append("Biomass CHP")
        elif ("boosthp") in x:
            AssignOC2.append("Booster Heat Pump")
        elif ("sthp") in x:
            AssignOC2.append("Solar thermal Heat Pump")
        elif ("stngboiler") in x:
            AssignOC2.append("Solar thermal with Natural gas boiler")
        elif ("stoilboiler") in x:
            AssignOC2.append("Solar thermal with oil boiler")
        elif ("stbiomassboiler") in x:
            AssignOC2.append("Solar thermal with biomass boiler")
        elif ("stelboiler") in x:
            AssignOC2.append("Solar thermal with el boiler")
        elif x.endswith('ac') is True:
            AssignOC2.append("Absorption Chiller")
        elif x.endswith('acec') is True:
            AssignOC2.append("Absorption Chiller with Electric Chiller")
        elif ("acngboiler") in x:
            AssignOC2.append("Absorption Chiller with Natural gas boiler")
        elif ("acoilboiler") in x:
            AssignOC2.append("Absorption Chiller with oil boiler")
        elif ("acbiomassboiler") in x:
            AssignOC2.append("Absorption Chiller with biomass boiler")
        elif ("acelectricboiler") in x:
            AssignOC2.append("Absorption Chiller with electric boiler")  
        elif ("acecngboiler") in x:
            AssignOC2.append("Absorption Chiller and Electric Chiller with Natural gas boiler")
        elif ("acecoilboiler") in x:
            AssignOC2.append("Absorption Chiller and Electric Chiller with oil boiler")
        elif ("acecbiomassboiler") in x:
            AssignOC2.append("Absorption Chiller and Electric Chiller with biomass boiler")
        elif ("acecelectricboiler") in x:
            AssignOC2.append("Absorption Chiller and Electric Chiller with electric boiler")
        elif ("acechp") in x:
            AssignOC2.append("Absorption Chiller and Electric Chiller with heat pump")
        elif ("achp") in x:
            AssignOC2.append("Absorption Chiller with heat pump")
        elif ("orc") in x:
            AssignOC2.append("Organic Rankine Cycle")
        elif ("exgrid") in x:
            AssignOC2.append("Existing Grid Technologies")
        elif("hp") in x:
            for i in streamidlistd:
                if(','.join(["str%dhp" % i ])) in x:
                    AssignOC2.append("Heat Pump") 
        else:
            AssignOC2.append(" ")

    AssignOC3= []

    for i in range(0, len(AssignOC1)):
        if AssignOC1[i] in AssignOC2[i]:
            AssignOC3.append(AssignOC2[i])
        elif AssignOC2[i] == '':
            AssignOC3.append(str(str(AssignOC1[i]) + str(AssignOC2[i])))
        else:
            AssignOC3.append(str(str(AssignOC1[i]) + ' ' + str(AssignOC4[i])+ ' ' + str(AssignOC2[i])))

    OperatingCost['Assignment'] = AssignOC3
    OperatingCost = OperatingCost.drop(['TECHNOLOGY'], axis = 1)
    OperatingCost = OperatingCost.drop(['NAME'], axis = 1)
    OperatingCost.rename(columns={"Assignment": "TECHNOLOGY"}, inplace=True)
    OperatingCost = OperatingCost [['VALUE', 'TECHNOLOGY']]

    figOC = px.bar(OperatingCost,x='TECHNOLOGY', y= 'VALUE')
    figOC.update_layout(
        title="Total Operating Cost",
        title_x=0.45,
        xaxis_title="Technologies",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Operating Cost in €",
        legend_title="Technologies",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )


    # source wise Operating Cost creation
    Techlist = OperatingCost["TECHNOLOGY"].tolist()
    Techlist
    AssignOC4 = []
    for x in Techlist:
        if "Source" in x:
            AssignOC4.append("Source")
        else:
            AssignOC4.append('')

    OperatingCost['Classification'] = AssignOC4
    Classlist = OperatingCost["Classification"].tolist()
    Classlist
    OperatingCostSource = OperatingCost.loc[OperatingCost["Classification"] == "Source"]
    del OperatingCostSource['Classification']
    Techlist = OperatingCostSource["TECHNOLOGY"].tolist()

    AssignOC5 = []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if str((','.join(["Source%d " % i ]))) in x:
                    AssignOC5.append(','.join(["Source%d" % i ]))

    OperatingCostSource['Classification'] = AssignOC5

    sourcelist = []
    for x in Techlist:
        for i in sourcesinkidlistd:
            if (','.join(["Source%d " % i ])) in x:
                sourcelist.append(','.join(["Source%d" % i ]))

    sourcelistd = []

    for i in sourcelist:
        if i not in sourcelistd:
            sourcelistd.append(i)

    ocso = []   
    for i in sourcesinkidlistd:
        if (','.join(["Source%d" % i ])) in sourcelistd:
            df = OperatingCostSource.loc[OperatingCostSource["Classification"] == (','.join(["Source%d" % i ]))]
            figsoOC = px.bar(df,x='TECHNOLOGY', y= 'VALUE')
            figsoOC.update_layout(
                title=(','.join(["Total OperatingCost for Source %d" % i ])),
                title_x=0.45,
                xaxis_title="Technologies",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Operating Cost in €",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )

            ocsouel = plotly.io.to_html(figsoOC, full_html=False,include_plotlyjs=False)
            ocso.append(ocsouel)


    # Sink wise graphs
    Techlist = OperatingCost["TECHNOLOGY"].tolist()
    Assign6OCsi= []
    for x in Techlist:
        if "Sink" in x:
            Assign6OCsi.append("Sink")
        else:
            Assign6OCsi.append('')
    OperatingCost['Classification'] = Assign6OCsi
    Classlist = OperatingCost["Classification"].tolist()

    OperatingCostSink = OperatingCost.loc[OperatingCost["Classification"] == "Sink"]
    del OperatingCostSink['Classification']
    Techlist = OperatingCostSink["TECHNOLOGY"].tolist()

    Assign7OCsi= []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if str((','.join(["Sink%d " % i ]))) in x:
                    Assign7OCsi.append(','.join(["Sink%d" % i ]))

    OperatingCostSink['Classification'] = Assign7OCsi

    sinklist = []

    for x in Techlist:
        for i in sourcesinkidlistd:
            if (','.join(["Sink%d " % i ])) in x:
                sinklist.append(','.join(["Sink%d" % i ]))

    sinklistd =[]   

    for i in sinklist:
        if i not in sinklistd:
            sinklistd.append(i)

    ocsi = []
    for i in sourcesinkidlistd:
        if (','.join(["Sink%d" % i ])) in sinklistd:
            df = OperatingCostSink.loc[OperatingCostSink["Classification"] == (','.join(["Sink%d" % i ]))]
            fig3siOC= px.bar(df, x='TECHNOLOGY', y= 'VALUE')
            fig3siOC.update_layout(
                title=(','.join(["Total Operating Cost for Sink %d" % i ])),
                title_x=0.45,
                xaxis_title="Technologies",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Operating Costt in €",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )     
            ocsiuel = plotly.io.to_html(fig3siOC, full_html=False,include_plotlyjs=False)
            ocsi.append(ocsiuel)  


    #Intial setup for production annual
    productionannualt = pd.DataFrame(a['ProductionByTechnology'])
    productionannual = productionannualt.pivot_table(values=['VALUE'], index=['YEAR'],columns=['TECHNOLOGY'],aggfunc=np.sum)
    productionannual = productionannual.reset_index()
    productionannual = productionannual.droplevel(level=0, axis=1)

    Tech_listPA = []
    Tech_listPA = productionannual.columns.tolist()
    Tech_listPA.remove('')
    Tech_listPA
    AssignPA1 = []
    AssignPA2= []
    AssignPA4 = []
    
    
    for x in Tech_listPA:
        if("grid") in x:
            AssignPA1.append("Grid Specific")
            AssignPA4.append('')
        elif ("dhn") in x:
            AssignPA1.append("District Heating Network")
            AssignPA4.append('')
        else:
            for i in sourcesinkidlistd:
                if (','.join(["sou%dstr" % i ])) in x:
                    AssignPA1.append(','.join(["Source%d" % i ]))
                elif (','.join(["sink%dstr" % i ])) in x:
                    AssignPA1.append(','.join(["Sink%d" % i ]))
            if "sou" or "sink" in x:
                for i in streamidlistd:
                    if(','.join(["str%d" % i ])) in x:
                        AssignPA4.append(','.join(["Stream%d" % i ]))
            else:
                AssignPA4.append('')
            for i in streamidlistd:
                if(','.join(["str%dsou" % i])) in x:
                    AssignPA1.append(','.join(["Source Stream%d" % i]))               

        if ("gridspecificngboiler") in x:
            AssignPA2.append("Grid Specific Natural gas Boiler")
        elif ("gridspecificoilboiler") in x:
            AssignPA2.append("Grid Specific Oil Boiler")
        elif ("gridspecificbioboiler") in x:
            AssignPA2.append("Grid Specific Biomass Boiler")
        elif ("gridspecifichp") in x:
            AssignPA2.append("Grid Specific Heat Pump")
        elif ("gridspecificsthp") in x:
            AssignPA2.append("Grid Specific solar thermal with Heat Pump")
        elif ("dhn") in x:
            AssignPA2.append("District Heating Network")
        elif ("she") in x:
            AssignPA2.append("Single Heat Exchanger")      
        elif ("mhe") in x:
            AssignPA2.append("Multiple Heat Exchanger")
        elif ("elwhrb") in x:
            AssignPA2.append("Electric Waste Heat Recovery Boiler")
        elif ("ngwhrb") in x:
            AssignPA2.append("Natural Gas Heat Recovery Boiler")
        elif ("oilwhrb") in x:
            AssignPA2.append("Oil Heat Recovery Boiler")
        elif ("biomasswhrb") in x:
            AssignPA2.append("Biomass Heat Recovery Boiler")
        elif ("chpng") in x:
            AssignPA2.append("Natural Gas CHP")
        elif ("chpoil") in x:
            AssignPA2.append("Oil CHP")
        elif ("chpbiomass") in x:
            AssignPA2.append("Biomass CHP")
        elif ("boosthp") in x:
            AssignPA2.append("Booster Heat Pump")
        elif ("sthp") in x:
            AssignPA2.append("Solar thermal Heat Pump")
        elif ("stngboiler") in x:
            AssignPA2.append("Solar thermal with Natural gas boiler")
        elif ("stoilboiler") in x:
            AssignPA2.append("Solar thermal with oil boiler")
        elif ("stbiomassboiler") in x:
            AssignPA2.append("Solar thermal with biomass boiler")
        elif ("stelboiler") in x:
            AssignPA2.append("Solar thermal with el boiler")
        elif x.endswith('ac') is True:
            AssignPA2.append("Absorption Chiller")
        elif x.endswith('acec') is True:
            AssignPA2.append("Absorption Chiller with Electric Chiller")
        elif ("acngboiler") in x:
            AssignPA2.append("Absorption Chiller with Natural gas boiler")
        elif ("acoilboiler") in x:
            AssignPA2.append("Absorption Chiller with oil boiler")
        elif ("acbiomassboiler") in x:
            AssignPA2.append("Absorption Chiller with biomass boiler")
        elif ("acelectricboiler") in x:
            AssignPA2.append("Absorption Chiller with electric boiler")  
        elif ("acecngboiler") in x:
            AssignPA2.append("Absorption Chiller and Electric Chiller with Natural gas boiler")
        elif ("acecoilboiler") in x:
            AssignPA2.append("Absorption Chiller and Electric Chiller with oil boiler")
        elif ("acecbiomassboiler") in x:
            AssignPA2.append("Absorption Chiller and Electric Chiller with biomass boiler")
        elif ("acecelectricboiler") in x:
            AssignPA2.append("Absorption Chiller and Electric Chiller with electric boiler")
        elif ("acechp") in x:
            AssignPA2.append("Absorption Chiller and Electric Chiller with heat pump")
        elif ("achp") in x:
            AssignPA2.append("Absorption Chiller with heat pump")
        elif ("orc") in x:
            AssignPA2.append("Organic Rankine Cycle")
        elif ("exgrid") in x:
            AssignPA2.append("Existing Grid Technologies")
        elif("hp") in x:
            for i in streamidlistd:
                if(','.join(["str%dhp" % i ])) in x:
                    AssignPA2.append("Heat Pump") 
        else:
            AssignPA2.append(" ")
    AssignPA3= ['']

    for i in range(0, len(AssignPA1)):
        if AssignPA1[i] in AssignPA2[i]:
            AssignPA3.append(AssignPA2[i])
        elif AssignPA2[i] == ' ':
            AssignPA3.append(str(str(AssignPA1[i]) + str(AssignPA2[i])))
        else:
            AssignPA3.append(str(str(AssignPA1[i]) + ' ' + str(AssignPA4[i])+ ' '+ str(AssignPA2[i])))


    productionannual.columns = AssignPA3


    #Production annual source aggregated
    
    collist = productionannual.columns.tolist()
    sourcelist = ['']
    for i in collist:
        if 'Source' in i:
            sourcelist.append(i)
    productionannualsourceplot = productionannual[sourcelist]
    list4PAplotsource = productionannualsourceplot.columns.tolist()
    list4PAplotsource.remove('')

    figsPAsource = px.bar(productionannualsourceplot, x='', y=list4PAplotsource)
    figsPAsource.update_layout(
        title="Annual heat generation for sources",
        title_x=0.45,
        xaxis_title="Year",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Production in kWh",
        legend_title="Technologies",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )

    #Production annual source aggregated

    collist = productionannual.columns.tolist()
    sourcelist = ['']
    for i in collist:
        if 'Source' in i:
            sourcelist.append(i)
    productionannualsourceplot = productionannual[sourcelist]
    list4PAplotsource = productionannualsourceplot.columns.tolist()
    list4PAplotsource.remove('')

    figsPAsource = px.bar(productionannualsourceplot, x='', y=list4PAplotsource)
    figsPAsource.update_layout(
        title="Annual heat generation for sources",
        title_x=0.45,
        xaxis_title="Year",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Production in kWh",
        legend_title="Technologies",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )

    #Production annual sink aggregated

    sinklist = ['']
    for i in collist:
        if 'Sink' in i:
            sinklist.append(i)
    productionannualsinkplot = productionannual[sinklist]
    list4PAplotsink = productionannualsinkplot.columns.tolist()
    list4PAplotsink.remove('')


    figsPAsink = px.bar(productionannualsinkplot, x='', y=list4PAplotsink)
    figsPAsink.update_layout(
        title="Annual heat or cold consumption for sinks",
        title_x=0.45,
        xaxis_title="Timeslice",
        paper_bgcolor='#FFFFFF',
        yaxis_title="Production in kWh",
        legend_title="Technologies",
        font=dict(
            family="Times New Roman",
            size=12,
            color="Black"
        )
    )

    #Production annual each source

    pagso = []

    for i in sourcesinkidlistd:
        eachsouPAlist = ['']
        for x in list4PAplotsource:
            if (','.join(["Source%d" % i ])) in x:
                eachsouPAlist.append(x)  
        if len(eachsouPAlist) > 1:
            productionannualeachsourceplot = productionannualsourceplot[eachsouPAlist]
            listPAeachsource = productionannualeachsourceplot.columns.tolist()
            listPAeachsource.remove('')
            figsPAeachsource = px.bar(productionannualeachsourceplot, x='', y=listPAeachsource)
            figsPAeachsource.update_layout(
                title=(','.join(["Annual heat generation for Source %d" % i ])),
                title_x=0.45,
                xaxis_title="Year",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Production in kWh",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )
            pasoel = plotly.io.to_html(figsPAeachsource, full_html=False,include_plotlyjs=False)
            pagso.append(pasoel)


    #Production annual each sink

    pagsi = []

    for i in sourcesinkidlistd:
        eachsinkPAlist = ['']
        for x in list4PAplotsink:
            if (','.join(["Sink%d " % i ])) in x:
                eachsinkPAlist.append(x)  
        if len(eachsinkPAlist) > 1:
            productionannualeachsinkplot = productionannualsinkplot[eachsinkPAlist]
            listPAeachSink = productionannualeachsinkplot.columns.tolist()
            listPAeachSink.remove('')
            figsPAeachSink = px.bar(productionannualsinkplot, x='', y=listPAeachSink)
            figsPAeachSink.update_layout(
                title=(','.join(["Annual heat or cold consumption for Sink %d" % i ])),
                title_x=0.45,
                xaxis_title="Year",
                paper_bgcolor='#FFFFFF',
                yaxis_title="Production in kWh",
                legend_title="Technologies",
                font=dict(
                    family="Times New Roman",
                    size=12,
                    color="Black"
                )
            )
            pasiel = plotly.io.to_html(figsPAeachSink, full_html=False,include_plotlyjs=False)
            pagsi.append(pasiel)

    #Pie charts
    #SOurce Pie

    productionannualpie = productionannualt.pivot_table(values=['VALUE'], index=['TECHNOLOGY'],aggfunc=np.sum)
    techlist = productionannualpie.index.tolist()

    productionannualpie['Tech'] = techlist
    productionannualpie = productionannualpie.reset_index()
    productionannualpie.drop('Tech', inplace=True, axis=1)
    techlist = productionannualpie['TECHNOLOGY'].tolist()
    classlist = []
    for x in techlist:
        if 'sink' in x:
            classlist.append('Sink')
        elif 'sou' in x:
            classlist.append('Source')
        else:
            classlist.append(' ')
    productionannualpie['Class'] = classlist
    productionannualpie

    productionannualsourcepie = productionannualpie.loc[productionannualpie['Class'] == 'Source']
    productionannualsourcepie

    sourcelist1 = productionannualsourcepie['TECHNOLOGY'].tolist()
    Assignpiesou = []
    for x in sourcelist1:
        for i in sourcesinkidlistd:
                if (','.join(["sou%dstr" % i ])) in x:
                    Assignpiesou.append(','.join(["Source%d" % i ]))
                elif x.endswith(','.join(["sou%d" % i ])) is True:
                    Assignpiesou.append('stream')
    productionannualsourcepie['source'] = Assignpiesou
    productionannualsourcepie = productionannualsourcepie.loc[productionannualsourcepie['source'] != 'stream']
    productionannualsourcepie = productionannualsourcepie.pivot_table(productionannualsourcepie,columns=['source'],aggfunc=np.sum)

    piecollistsource = productionannualsourcepie.columns.tolist()
    pievallistsource = productionannualsourcepie.values.tolist()
    pievalflatlistsource = []
    for sublist in pievallistsource:
        for item in sublist:
            pievalflatlistsource.append(item)
    productionannualsourcepieplot = pd.DataFrame()
    productionannualsourcepieplot['Total Production'] =  pievalflatlistsource
    productionannualsourcepieplot['Sources'] =  piecollistsource
    productionannualsourcepieplot
    figpiesource = px.pie(productionannualsourcepieplot, values='Total Production', names='Sources', title='Share of excess heat generation')

    productionannualsinkpie = productionannualpie.loc[productionannualpie['Class'] == 'Sink']
    sinklist1 = productionannualsinkpie['TECHNOLOGY'].tolist()
    Assignpiesink = []
    for x in sinklist1:
        for i in sourcesinkidlistd:
                if (','.join(["sink%dstr" % i ])) in x:
                    Assignpiesink.append(','.join(["Sink%d" % i ]))
    productionannualsinkpie['sink'] = Assignpiesink
    productionannualsinkpie = productionannualsinkpie.pivot_table(productionannualsinkpie,columns=['sink'],aggfunc=np.sum)

    piecollistsink = productionannualsinkpie.columns.tolist()
    pievallistsink = productionannualsinkpie.values.tolist()
    pievalflatlistsink = []
    for sublist in pievallistsink:
        for item in sublist:
            pievalflatlistsink.append(item)
    productionannualsinkpieplot = pd.DataFrame()
    productionannualsinkpieplot['Total Production'] =  pievalflatlistsink
    productionannualsinkpieplot['Sources'] =  piecollistsink
    productionannualsinkpieplot
    figpiesink = px.pie(productionannualsinkpieplot, values='Total Production', names='Sources', title='Share of excess heat consumption')
    
        # Accumulated new capacity table

    AccumulatedNewCapacitydf = AccumulatedNewCapacityplot.loc[AccumulatedNewCapacityplot[''] == AccumulatedNewCapacityplot[''].max()]
    del AccumulatedNewCapacitydf['']
    AccumulatedNewCapacitydf.reset_index(drop=True)
    AccumulatedNewCapacitydf.reset_index(drop=True, inplace=True)
    AccumulatedNewCapacitydf = AccumulatedNewCapacitydf.rename_axis(None, axis=1)
    AccumulatedNewCapacitydf = AccumulatedNewCapacitydf.round(decimals=2)
    AccumulatedNewCapacitydf1 = AccumulatedNewCapacitydf.to_html(index=False, col_space= 100, justify='center')
    AccumulatedNewCapacitytable = AccumulatedNewCapacitydf1.replace('<tr>', '<tr align="center">')

    # Annual Emissions table

    AnnualTechnologyEmissiondf = AnnualTechnologyEmission.pivot_table(AnnualTechnologyEmission,columns=['TECHNOLOGY'],aggfunc=np.sum)
    AnnualTechnologyEmissiondf.reset_index(drop=True, inplace=True)
    AnnualTechnologyEmissiondf = AnnualTechnologyEmissiondf.rename_axis(None, axis=1)
    AnnualTechnologyEmissiondf = pd.DataFrame()
    AnnualTechnologyEmissiondf1 = AnnualTechnologyEmissiondf.to_html(index=False, col_space= 100, justify='center')
    AnnualTechnologyEmissiondtable = AnnualTechnologyEmissiondf1.replace('<tr>', '<tr align="center">')

    # Accumulated new Storage capacity table

    AccumulatedNewStorageCapacitydf  = AccumulatedNewStorageCapacityplot.loc[AccumulatedNewStorageCapacityplot[''] == AccumulatedNewStorageCapacityplot[''].max()]
    del AccumulatedNewStorageCapacitydf['']
    AccumulatedNewStorageCapacitydf.reset_index(drop=True)
    AccumulatedNewStorageCapacitydf.reset_index(drop=True, inplace=True)
    AccumulatedNewStorageCapacitydf = AccumulatedNewStorageCapacitydf.rename_axis(None, axis=1)
    AccumulatedNewStorageCapacitydf = AccumulatedNewStorageCapacitydf.round(decimals=2)
    AccumulatedNewStorageCapacitydf1 = AccumulatedNewStorageCapacitydf.to_html(index=False, col_space= 100, justify='center')
    AccumulatedNewStorageCapacitytable = AccumulatedNewStorageCapacitydf1.replace('<tr>', '<tr align="center">')
    AccumulatedNewStorageCapacitydf

    # Capital costs table
    # del CapitalInvestment['Classification']
    CapitalInvestmenttable1 = CapitalInvestment.pivot_table(CapitalInvestment,columns=['TECHNOLOGY'],aggfunc=np.sum)
    CapitalInvestmenttable1.reset_index(drop=True)
    CapitalInvestmenttable1.reset_index(drop=True, inplace=True)
    CapitalInvestmenttable1 = CapitalInvestmenttable1.rename_axis(None, axis=1)
    CapitalInvestmenttable1 = CapitalInvestmenttable1.round(decimals=2)
    CapitalInvestmenttabledf1 =  CapitalInvestmenttable1.to_html(index=False, col_space= 100, justify='center')
    CapitalInvestmenttable = CapitalInvestmenttabledf1.replace('<tr>', '<tr align="center">')


    # Operating costs table
    # del OperatingCost['Classification']
    OperatingCostTable1 = OperatingCost.pivot_table(OperatingCost,columns=['TECHNOLOGY'],aggfunc=np.sum)
    OperatingCostTable1.reset_index(drop=True)
    OperatingCostTable1.reset_index(drop=True, inplace=True)
    OperatingCostTable1 = OperatingCostTable1.rename_axis(None, axis=1)
    OperatingCostTabledf1 =  OperatingCostTable1.to_html(index=False, col_space= 100, justify='center')
    OperatingCosttable = OperatingCostTabledf1.replace('<tr>', '<tr align="center">')

    # Capital costs storage table
    CapitalInvestmentsto1 = CapitalInvestmentsto.pivot_table(CapitalInvestmentsto,columns=['STORAGE'],aggfunc=np.sum)
    CapitalInvestmentsto1.reset_index(drop=True)
    CapitalInvestmentsto1.reset_index(drop=True, inplace=True)
    CapitalInvestmentsto1 = CapitalInvestmentsto1.rename_axis(None, axis=1)
    CapitalInvestmentsto1 = CapitalInvestmentsto1.round(decimals=2)
    CapitalInvestmentstodf1 =  CapitalInvestmentsto1.to_html(index=False, col_space= 100, justify='center')
    CapitalInvestmentstotable = CapitalInvestmentstodf1.replace('<tr>', '<tr align="center">')

    # Production annual sources table
    productionannualsourceplot.reset_index(drop=True)
    productionannualsourceplot.reset_index(drop=True, inplace=True)
    productionannualsourceplot = productionannualsourceplot.rename_axis(None, axis=1)
    productionannualsourceplot = productionannualsourceplot.round(decimals=2)
    productionannualsourceplot.rename(columns={"": "YEAR"}, inplace=True)
    productionannualsourceplotdf1 =  productionannualsourceplot.to_html(index=False, col_space= 100, justify='center')
    productionannualsourcetable = productionannualsourceplotdf1.replace('<tr>', '<tr align="center">')

    # Production annual sinks table
    productionannualsinkplot.reset_index(drop=True)
    productionannualsinkplot.reset_index(drop=True, inplace=True)
    productionannualsinkplot = productionannualsinkplot.rename_axis(None, axis=1)
    productionannualsinkplot = productionannualsinkplot.round(decimals=2)
    productionannualsinkplot.rename(columns={"": "YEAR"}, inplace=True)
    productionannualsinkplotdf1 =  productionannualsinkplot.to_html(index=False, col_space= 100, justify='center')
    productionannualsinkplottable = productionannualsinkplotdf1.replace('<tr>', '<tr align="center">')

    #Total excess heat production

    productionannualsourcepie.reset_index(drop=True)
    productionannualsourcepie.reset_index(drop=True, inplace=True)
    productionannualsourcepie = productionannualsourcepie.rename_axis(None, axis=1)
    productionannualsourcepie = productionannualsourcepie.round(decimals=2)
    productionannualsourcepiedf1 =  productionannualsourcepie.to_html(index=False, col_space= 100, justify='center')
    productionannualsourcepietable = productionannualsourcepiedf1.replace('<tr>', '<tr align="center">')


    #Total excess heat consumption

    productionannualsinkpieplot.reset_index(drop=True)
    productionannualsinkpieplot.reset_index(drop=True, inplace=True)
    productionannualsinkpieplot = productionannualsinkpieplot.rename_axis(None, axis=1)
    productionannualsinkpieplot = productionannualsinkpieplot.round(decimals=2)
    productionannualsinkpieplot.rename(columns={"Total Production": "Total Consumption in kWh"}, inplace=True)
    productionannualsinkpieplotdf1 =  productionannualsinkpieplot.to_html(index=False, col_space= 100, justify='center')
    productionannualsinkpieplottable = productionannualsinkpieplotdf1.replace('<tr>', '<tr align="center">')
    
    

    combinedaccnewcap = plotly.io.to_html(fig, full_html=False,include_plotlyjs=False)
    if "Grid Specific" in Assign8:
        gridaccnewcap = plotly.io.to_html(fig4, full_html=False,include_plotlyjs=False)
    else:
        gridaccnewcap = ''    
    accsto = plotly.io.to_html(figsto, full_html=False,include_plotlyjs=False)
    emallcomb = plotly.io.to_html(figem, full_html=False,include_plotlyjs=False)
    if "Grid Specific" in Assign8em:
        emgridspec = plotly.io.to_html(figemgrid, full_html=False,include_plotlyjs=False)
    else:
        emgridspec = ''
    ciac = plotly.io.to_html(figCI, full_html=False,include_plotlyjs=False)
    cisto = plotly.io.to_html(figCIS, full_html=False,include_plotlyjs=False)
    cioc = plotly.io.to_html(figOC, full_html=False,include_plotlyjs=False)
    pasou = plotly.io.to_html(figsPAsource, full_html=False,include_plotlyjs=False) 
    pasi = plotly.io.to_html(figsPAsink, full_html=False,include_plotlyjs=False) 
    piesou = plotly.io.to_html(figpiesource, full_html=False,include_plotlyjs=False) 
    piesi =  plotly.io.to_html(figpiesink, full_html=False,include_plotlyjs=False) 

    ### REPORT_RENDERING_CODE [BEGIN]

    script_dir = os.path.dirname(__file__)

    env = Environment(
        loader=FileSystemLoader(os.path.join(script_dir, "asset")),
        autoescape=False
    )

    template = env.get_template('index-short.template.html')
    template_content = template.render(ANCT_df=AccumulatedNewCapacitytable,PIESOU=piesou, ANCSOU=ancsou, ANCSI=ancsi, EMSO=emso, EMSI=emsi, CISO=ciso, CICI=cisi, OCSO=ocso, OCSI=ocsi, PEISI=piesi, PAGSO=pagso, PAGSI=pagsi, PASOU=pasou, ANCAC=combinedaccnewcap,PASI=pasi, CIOC=cioc, ACSTO=accsto,CISTO=cisto, EMALLCOMB=emallcomb, EMGRIDSPEC=emgridspec,CIAC=ciac, ANCGS=gridaccnewcap, ANST_df=AccumulatedNewStorageCapacitytable, AHTSO_df=productionannualsourcetable, AHTSI_df=productionannualsinkplottable, TOTSO_df=productionannualsourcepietable, TOTSI_df=productionannualsinkpieplottable, CISTO_df=CapitalInvestmentstotable, TOTEM_df=AnnualTechnologyEmissiondtable, CI_df=CapitalInvestmenttable, OC_df=OperatingCosttable)

    
    return(template_content)
    
    