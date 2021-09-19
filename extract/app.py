from re import S
from flask import Flask, request, jsonify 
from flask_cors import CORS
import json
from world_get_data import energy_per_capita, most_common_energy, renewable_energy_share, energy_trends, energy_trends_share
from us_get_data import state_share_energy, co2_by_source, emissions_by_state, total_energy_calc
app = Flask(__name__)
dict1 = {"USA": {"Number in Household": 3, "House Size": 1000, "AC Use": 10, "Heating Use": 10, "Electric Water Heater": 5, 
"Fridges and Freezers": 0, "Large Kitchen Appliances": 3, "Small Kitchen Appliances": 3, "Washing Machine Loads": 3, 
"Dryer Loads": 5, "Dishwasher": 2, "Bathroom Electronics": 2, "Laptops and Desktops": 10, "Television": 2, "Smart-home": 3,
"Other Electronics": 10}}
x = json.dumps(dict1, indent=3)
print(x)

@app.route("/survey", methods=["POST"])
def calc_score():
    score = 0
    country = ""
    dict = request.get_json(force = True)
    for i in dict.keys():
        country = i
    household = dict[country]["Number in Household"]
    size = dict[country]["House Size"]
    ac = dict[country]["AC Use"]
    heating = dict[country]["Heating Use"]
    water_heater = dict[country]["Electric Water Heater"]
    fridges = dict[country]["Fridges and Freezers"]
    large_kitchen = dict[country]["Large Kitchen Appliances"]
    small_kitchen = dict[country]["Small Kitchen Appliances"]
    washing_machine = dict[country]["Washing Machine Loads"]
    dryer = dict[country]["Dryer Loads"]
    dishwasher = dict[country]["Dishwasher"]
    bathroom_electronics = dict[country]["Bathroom Electronics"]
    laptops = dict[country]["Laptops and Desktops"]
    tv = dict[country]["Television"]
    smart_home = dict[country]["Smart-home"]
    other_electronics = dict[country]["Other Electronics"]

    return jsonify(str(3*ac*size + 10*heating*size + 700*fridges + 1500*large_kitchen + 800*small_kitchen
    + 1200*washing_machine + 5400*dryer + 1500*dishwasher + 1300*bathroom_electronics + 75*laptops
    + 75*tv + 15*smart_home + 75*other_electronics))

@app.route("/energypercapita", methods=["POST"])
def energy_per_cap():
    year = -1
    energy_per_capita_dict = energy_per_capita()
    print(energy_per_capita_dict)
    dict = request.get_json(force = True)
    for i in range(len(dict.keys())):
        if i == 0:
            country =  dict["country"]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(energy_per_capita_dict[country][str(year)])
    else:
        return jsonify(energy_per_capita_dict[country])

@app.route("/mostusedenergy", methods=["POST"])
def most_used_energy():
    year = -1
    most_common_dict = most_common_energy()
    print(most_common_dict)
    dict = request.get_json(force = True)
    for i in range(len(dict.keys())):
        if i == 0:
            country =  dict["country"]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(most_common_dict[country][str(year)])
    else:
        return jsonify(most_common_dict[country])

@app.route("/renewableshare", methods=["POST"])
def renewable_share_energy():
    year = -1
    renewable_dict = renewable_energy_share()
    dict = request.get_json(force = True)
    for i in range(len(dict.keys())):
        if i == 0:
            country =  dict["country"]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(renewable_dict[country][str(year)])
    else:
        return jsonify(renewable_dict[country])

@app.route("/energytrends", methods=["POST"])
def energy_consump_trend():
    year = -1
    energy_dict = energy_trends()
    dict = request.get_json(force = True)
    for i in range(len(dict.keys())):
        if i == 0:
            country =  dict["country"]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(energy_dict[country][str(year)])
    else:
        return jsonify(energy_dict[country])

@app.route("/energysharetrends", methods=["POST"])
def energy_share_trend():
    year = -1
    energy_share_dict = energy_trends_share()
    dict = request.get_json(force = True)
    for i in range(len(dict.keys())):
        if i == 0:
            country =  dict["country"]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(energy_share_dict[country][str(year)])
    else:
        return jsonify( energy_share_dict[country])

@app.route("/stateshareenergy", methods=["POST"])        
def state_share():
    year = -1
    state_share_dict = state_share_energy()
    dict = request.get_json(force = True)
    for i in range(len(dict.keys())):
        if i == 0:
            state=  dict["state"]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(state_share_dict[state][str(year)])
    else:
        return jsonify(state_share_dict[state])

@app.route("/stateemissions", methods=["POST"])        
def state_emissions():
    year = -1
    state_emissions_dict = emissions_by_state()
    total_energy_dict = total_energy_calc()
    dict = request.get_json(force = True)
    for i in range(len(dict.keys())):
        if i == 0:
            state=  dict["state"]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(str(float(state_emissions_dict[state][str(year)])/(float(total_energy_dict[state][str(year)]))))
    else:
        ratio_dict = {}
        for i in range(30):
            ratio_dict[str(1990+i)] = float(state_emissions_dict[state][str(1990+i)]) / float(total_energy_dict[state][str(1990+i)])
        return jsonify(ratio_dict)

@app.route("/statesourceemissions", methods=["POST"])
def state_emissions_by_source():
    year = -1
    state_source_emissions_dict = co2_by_source()
    total_energy_dict = total_energy_calc()
    dict = request.get_json(force = True)
    for i in range(len(dict.keys())):
        if i == 0:
            state=  dict["state"]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(state_source_emissions_dict[state][str(year)])
    else:
        return jsonify(state_source_emissions_dict[state])


        
    



