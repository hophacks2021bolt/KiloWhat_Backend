import pandas as pd
import os.path
import json

owid_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/owid-energy-data.csv')
eia_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/annual_generation_state-3.xls')
owid_cols = ["country", "year", "energy_per_capita", "renewables_share_energy", "biofuel_share_energy", "coal_share_energy",
"gas_share_energy", "nuclear_share_energy", "hydro_share_energy", "oil_share_energy", "solar_share_energy", "wind_share_energy",
"biofuel_consumption", "coal_consumption", "gas_consumption", "nuclear_consumption", "hydro_consumption", "oil_consumption", 
"solar_consumption", "wind_consumption"]
sources = ["biofuel", "coal","gas", "nuclear", "hydro", "oil", "solar", "wind"]

df = pd.read_csv(owid_path, usecols=owid_cols)
df_eia = pd.read_excel(eia_path)
def energy_per_capita():
    dict = {}
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): {"avgEnergyUsage": str(df["energy_per_capita"][x])}}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = {"avgEnergyUsage": str(df["energy_per_capita"][x])}
    return dict

def renewable_energy_share():
    dict = {}
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): {"renewableEnergyShare": str(df["renewables_share_energy"][x])}}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = {"renewableEnergyShare": str(df["renewables_share_energy"][x])}
    return dict

#Most common energy for each country, each year
def most_common_energy():
    dict = {}
    highest_share = ""
    max = 0
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            for i in sources:
                col = i + "_share_energy"
                if df[col][x] > max:
                    max = df[col][x]
                    highest_share = i
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): {"highestShare": highest_share}}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = {"highestShare": highest_share}
    return dict

def energy_trends():
    dict = {}
    temp_dict = {}
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            for i in sources:
                temp_dict[i] = str(df[i+"_consumption"][x])
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): json.dumps(temp_dict)}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = json.dumps(temp_dict)
    return dict

def energy_trends_share():
    dict = {}
    temp_dict = {}
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            for i in sources:
                temp_dict[i] = str(df[i+"_share_energy"][x])
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): json.dumps(temp_dict)}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = json.dumps(temp_dict)
    return dict
