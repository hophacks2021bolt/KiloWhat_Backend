from re import S
from flask import Flask, request, jsonify 
from flask_cors import CORS
import json
from world_get_data import energy_per_capita, most_common_energy, renewable_energy_share, energy_trends, energy_trends_share
from us_get_data import state_share_energy, co2_by_source, emissions_by_state, total_energy_calc
app = Flask(__name__)
CORS(app)
dict1 = {"USA": {"Number in Household": 3, "House Size": 1000, "AC Use": 10, "Heating Use": 10, "Electric Water Heater": 5, 
"Fridges and Freezers": 0, "Large Kitchen Appliances": 3, "Small Kitchen Appliances": 3, "Washing Machine Loads": 3, 
"Dryer Loads": 5, "Dishwasher": 2, "Bathroom Electronics": 2, "Laptops and Desktops": 10, "Television": 2, "Smart-home": 3,
"Other Electronics": 10}}
x = json.dumps(dict1, indent=3)
print(x)
states = {'Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'American Samoa': 'AS', 'Arizona': 'AZ', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Guam': 'GU', 'Hawaii': 'HI', 'Iowa': 'IA', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Massachusetts': 'MA', 'Maryland': 'MD', 'Maine': 'ME', 'Michigan': 'MI', 'Minnesota': 'MN', 'Missouri': 'MO', 'Northern Mariana Islands': 'MP', 'Mississippi': 'MS', 'Montana': 'MT', 'National': 'NA', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Nebraska': 'NE', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'Nevada': 'NV', 'New York': 'NY', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Virginia': 'VA', 'Virgin Islands': 'VI', 'Vermont': 'VT', 'Washington': 'WA', 'Wisconsin': 'WI', 'West Virginia': 'WV', 'Wyoming': 'WY'}
@app.route("/survey", methods=["POST"])
def calc_score():
    score = 0
    country = ""
    dict = request.get_json(force = True)
    for i in dict.keys():
        country = i
    household = int(dict[country]["Number in Household"])

    size_dict = {0:2000,1:1000,2:1250,3:1750,4:2250,5:2750,6:3000}
    size = size_dict[dict[country]["House Size"]]

    ac_dict = {"0":7,"1":0,"2":2.5,"3":6.5,"4":10.5,"5":14.5,"6":18.5,"7":22.5}
    score += 3*ac_dict[dict[country]["AC Use"]]*size

    heat_dict = {"0":7,"1":0,"2":2.5,"3":6.5,"4":10.5,"5":14.5,"6":18.5,"7":22.5}
    score += 10*heat_dict[dict[country]["Heating Use"]]*size

    score += 700*int(dict[country]["Fridges and Freezers"])

    score += 1500*int(dict[country]["Large Kitchen Appliances"])
    score +=800*int(dict[country]["Small Kitchen Appliances"])
    washing_dict = {"0":3,"1":0,"2":1.5,"3":3.5,"4":5.5,"5":7}
    score += 1200/7*washing_dict[dict[country]["Washing Machine Loads"]]
    score += 5400/7*washing_dict[dict[country]["Dryer Loads"]]
    score += 1500*washing_dict[dict[country]["Dishwasher"]]
    score += 1300*washing_dict[dict[country]["Bathroom Electronics"]]
    score += 75*washing_dict[dict[country]["Laptops and Desktops"]]
    score += 75*washing_dict[dict[country]["Television"]]
    score += 12*washing_dict[dict[country]["Smart-home"]]
    score += 75*washing_dict[dict[country]["Other Electronics"]]

    return jsonify(str(365*score))

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
            state=  states[dict["state"]]
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
            state=  states[dict["state"]]
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
            state=  states[dict["state"]]
        else: 
            year = dict["year"]
    if year != -1:
        return jsonify(state_source_emissions_dict[state][str(year)])
    else:
        return jsonify(state_source_emissions_dict[state])


        
    



