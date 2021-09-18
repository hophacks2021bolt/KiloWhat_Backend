import pandas as pd
import os.path
import json

owid_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/owid-energy-data.csv')
owid_cols = ["country", "year", "energy_per_capita", "renewables_share_energy", "biofuel_share_energy", "coal_share_energy",
"gas_share_energy", "nuclear_share_energy", "hydro_share_energy", "oil_share_energy", "solar_share_energy", "wind_share_energy"]

sources = ["biofuel", "coal","gas", "nuclear", "hydro", "oil", "solar", "wind"]

df = pd.read_csv(owid_path, usecols=owid_cols)

def energy_per_capita():
    dict = {}
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): {"avgEnergyUsage": str(df["energy_per_capita"][x])}}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = {"avgEnergyUsage": str(df["energy_per_capita"][x])}
    return json.dumps(dict, indent=3)

def renewable_energy_share():
    dict = {}
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): {"renewableEnergyShare": str(df["renewables_share_energy"][x])}}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = {"renewableEnergyShare": str(df["renewables_share_energy"][x])}
    return json.dumps(dict, indent = 3)

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
    return json.dumps(dict, indent = 3)
"""
def energy_trends():
    dict = {}
    col = ""
    source = ""
    consump_val = []
    temp_dict = {}
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            for i in sources:
                print(df["solar_consumption"][x])
                temp_dict[i] = df[i+"_consumption"][x]
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): temp_dict}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = {"highestShare": highest_share}
    with open('data.json', 'w') as f:
        json.dump(dict, f)
energy_trends()
"""