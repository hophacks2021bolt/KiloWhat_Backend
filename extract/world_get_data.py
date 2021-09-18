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
#print(df_eia['STATE'])
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
    return json.dumps(dict, indent = 3)

def energy_trends():
    dict = {}
    temp_dict = {}
    for x in range(len(df["country"])):
        if (df["year"][x] >= 1990):
            for i in sources:
                temp_dict[i] = str(df[i+"_consumption"][x])
                #print(str(df[i+"_consumption"][x]))
            if df["country"][x] not in dict:
                dict[df["country"][x]] = {str(df["year"][x]): json.dumps(temp_dict)}
            else:
                dict[df["country"][x]] [str(df["year"][x])] = json.dumps(temp_dict)
    return json.dumps(dict, indent=3)

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
    return json.dumps(dict, indent=3)
def get_total_energy(list_of_energy):
    total_energy = 0
    share_energy = []
    inc = 0
    for i in list_of_energy:
        total_energy = total_energy + i
    return total_energy

def state_energy():
    dict = {}
    temp_dict = {}
    state = ""
    energy = 0
    coal = 0
    nuclear = 0
    hydro = 0
    solar = 0
    gas = 0
    geo = 0
    wind = 0
    petrol = 0
    for x in range(len(df_eia["YEAR"])):
        if (df_eia["YEAR"][x] >= 1990):
            if df_eia["STATE"][x] not in dict:
                energy = 0
                coal = 0
                nuclear = 0
                hydro = 0
                solar = 0
                gas = 0
                geo = 0
                wind = 0
                petrol = 0
                total_energy = 1
                source = df_eia["ENERGY SOURCE"][x]
                if source == "Petroleum":
                    petrol = petrol + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Hydroelectric Conventional":
                    hydro = hydro + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Nuclear":
                    nuclear = nuclear + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Natural Gas":
                    gas = gas + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Coal":
                    coal = coal + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Geothermal":
                    geo = geo + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Solar Thermal and Photovoltaic":
                    solar = solar + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Wind":
                    wind = wind + df_eia["GENERATION (Megawatthours)"][x]
                temp_dict["Petroleum"] = petrol
                temp_dict["Hydroelectric Conventional"] = hydro
                temp_dict["Nuclear"] = nuclear
                temp_dict["Natural Gas"] = gas
                temp_dict["Coal"] = coal
                temp_dict["Geothermal"] = geo
                temp_dict["Solar Thermal and Photovoltaic"] = solar
                temp_dict["Wind"] = wind
                dict[df_eia["STATE"][x]] = {str(df_eia["YEAR"][x]): json.dumps(temp_dict)}
            else:
                source = df_eia["ENERGY SOURCE"][x]
                if source == "Petroleum":
                    petrol = petrol + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Hydroelectric Conventional":
                    hydro = hydro + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Nuclear":
                    nuclear = nuclear + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Natural Gas":
                    gas = gas + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Coal":
                    coal = coal + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Geothermal":
                    geo = geo + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Solar Thermal and Photovoltaic":
                    solar = solar + df_eia["GENERATION (Megawatthours)"][x]
                elif source == "Wind":
                    wind = wind + df_eia["GENERATION (Megawatthours)"][x]
                total_energy = get_total_energy([petrol, hydro, nuclear, gas, coal, geo, solar, wind])
                temp_dict["Petroleum"] = petrol / total_energy
                temp_dict["Hydroelectric Conventional"] = hydro / total_energy
                temp_dict["Nuclear"] = nuclear / total_energy
                temp_dict["Natural Gas"] = gas / total_energy
                temp_dict["Coal"] = coal / total_energy
                temp_dict["Geothermal"] = geo / total_energy
                temp_dict["Solar Thermal and Photovoltaic"] = solar / total_energy
                temp_dict["Wind"] = wind / total_energy
                dict[df_eia["STATE"][x]] [str(df_eia["YEAR"][x])] = json.dumps(temp_dict)
    return json.dumps(dict, indent=3)
print(state_energy())