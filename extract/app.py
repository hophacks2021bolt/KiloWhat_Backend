from flask import Flask, request, jsonify 
from flask_cors import CORS
import json
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


        
    



