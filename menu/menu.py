import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient(host='db_menu', port=27019, username='menu', password='12345')
#switch to db fakeUberEat
db = client.fakeUberEat

@app.route('/')
def todo():
    try:
        serverInfo = client.server_info()
    except:
        return "Server not available"
    return f"Connect to the MongoDB server."

#/group: Return a JSON object with the group number and group member information.
@app.route ('/group', methods=['GET'])
def group():
    return jsonify({"group_number": "5", "group_members":[{"Name": "Wong Pan Chi", "Student_ID": "18063466D"},{"Name": "Wong Kin Sang", "Student_ID": "18051915D"},{"Name": "Yuen Chun Ming", "Student_ID": "18059819D"},{"Name": "Sin Kwo Yin", "Student_ID": "18059048D"}]}), 200

# Return the API using
@app.route ('/api', methods=['GET'])
def whereami():
    return jsonify({"API":"menu"}), 200



#/menus: Return a JSON object with all the menus’ attributes
@app.route ('/stores/<store_id>/menus', methods=['GET'])
def get_menu(store_id):
    #The menus sorted in ascending order of store ID.
    # menus =db.menu.find({},{"_id" : 0}).sort("store_id", 1)
    #db = uber_eat_db()
    menu = db['menu'].find({"store_id": store_id})

    
    result = []
    
    print(db["menu"].count_documents({"store_id": store_id}))
    # if the store exist, append it to output list.
    if (db["menu"].count_documents({"store_id": store_id}) > 0):

        # find the student with unique student_id
        menu = db['menu'].find({"store_id": store_id},{"_id" : 0})

        # add the student attributes into dictionary
        for item in menu:
            menu_dict = {}
            for key, value in item.items():
                if (key == "dishes_name" or key == "price"):
                    if(type(value) != str):
                        menu_dict[key] = value
                    else:
                        menu_dict[key] = str(value)
            result.append(menu_dict)
    
    # return error msg if student not found.
    else:
        return jsonify({"error": "not found"}), 404

    return jsonify(result),200

# create or update the entire menu for a specific store.
@app.route ('/stores/<store_id>/menus', methods=['PUT'])
def update_menu(store_id):
    #The menus sorted in ascending order of store ID.
    menus =db.menu.find({},{"_id" : 0}).sort("store_id", 1)
    result = []
    for menu in menus:
        temp = {}
        for key, value in menu.items():
            if (type(menu[key])==str):
                temp[key] = str(menu[key])
            else:
                temp[key] = menu[key]
        result.append(temp)
    return jsonify(result),200

# updates an individual item within a menu.
@app.route ('/stores/<store_id>/menus/items/<item_id>', methods=['POST'])
def update_item(store_id, item_id):
    #The menus sorted in ascending order of store ID.
    menus =db.menu.find({},{"_id" : 0}).sort("store_id", 1)
    result = []
    for menu in menus:
        temp = {}
        for key, value in menu.items():
            if (type(menu[key])==str):
                temp[key] = str(menu[key])
            else:
                temp[key] = menu[key]
        result.append(temp)
    return jsonify(result),200
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=15000, debug=True)
