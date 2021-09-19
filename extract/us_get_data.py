import pandas as pd
import os.path
import json

eia_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/annual_generation_state-3.xls')
eia_emissions_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/emission_annual-3.xls')
price_path = eia_emissions_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/avgprice_annual.xlsx')
df_eia = pd.read_excel(eia_path)
df_emissions = pd.read_excel(eia_emissions_path)
df_cost = pd.read_excel(price_path)

def get_total_energy(list_of_energy):
    total_energy = 0
    share_energy = []
    inc = 0
    for i in list_of_energy:
        total_energy = total_energy + i
    return total_energy

def state_share_energy():
    dict = {}
    temp_dict = {}
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
    return dict

def total_energy_calc():
    dict = {}
    current_year = 1990
    for x in range(len(df_eia["YEAR"])):
        if (df_eia["YEAR"][x] >= 1990):
            if df_eia["STATE"][x] not in dict:
                energy = 0
                if df_eia["ENERGY SOURCE"][x] == "Total":
                    energy = energy + df_eia["GENERATION (Megawatthours)"][x]    
                dict[df_eia["STATE"][x]] = {str(df_eia["YEAR"][x]): str(energy)}
            else:
                if df_eia["ENERGY SOURCE"][x] == "Total":
                    energy = energy + df_eia["GENERATION (Megawatthours)"][x]
                dict[df_eia["STATE"][x]] [str(df_eia["YEAR"][x])] = str(energy)
    return dict

def emissions_by_state():
    dict = {}
    temp_dict = {}
    co2 = 0
    for x in range(len(df_emissions["Year"])):
        if (df_emissions["Year"][x] >= 1990):
            if df_emissions["State"][x] not in dict:
                co2 = 0
                if df_emissions["Energy Source"][x] == "All Sources":
                    co2 = co2 + df_emissions["CO2\n"][x]    
                dict[df_emissions["State"][x]] = {str(df_emissions["Year"][x]): str(co2)}
            else:
                if df_emissions["Energy Source"][x] == "All Sources":
                    co2 = co2 + df_emissions["CO2\n"][x]
                dict[df_emissions["State"][x]] [str(df_emissions["Year"][x])] = str(co2)
    return dict


def co2_by_source():
    dict = {}
    temp_dict = {}
    coal = 0
    gas = 0
    petrol = 0
    for x in range(len(df_emissions["Year"])):
        if (df_emissions["Year"][x] >= 1990):
            if df_emissions["State"][x] not in dict:
                coal = 0
                solar = 0
                gas = 0
                petrol = 0
                source = df_emissions["Energy Source"][x]
                if source == "Petroleum":
                    petrol = petrol + df_emissions["CO2\n"][x]
                elif source == "Coal":
                    coal = coal + df_emissions["CO2\n"][x]
                elif source == "Natural Gas":
                    gas = gas + df_emissions["CO2\n"][x]
                temp_dict["Petroleum"] = str(petrol)
                temp_dict["Natural Gas"] = str(gas)
                temp_dict["Coal"] = str(coal)
                dict[df_emissions["State"][x]] = {str(df_emissions["Year"][x]): json.dumps(temp_dict)}
            else:
                source = df_emissions["Energy Source"][x]
                if source == "Petroleum":
                    petrol = petrol + df_emissions["CO2\n"][x]
                elif source == "Coal":
                    coal = coal + df_emissions["CO2\n"][x]
                elif source == "Natural Gas":
                    gas = gas + df_emissions["CO2\n"][x]
                temp_dict["Petroleum"] = str(petrol)
                temp_dict["Natural Gas"] = str(gas)
                temp_dict["Coal"] = str(coal)
                dict[df_emissions["State"][x]] [str(df_emissions["Year"][x])] = json.dumps(temp_dict)
    return dict
