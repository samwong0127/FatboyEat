import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from prometheus_flask_exporter import PrometheusMetrics
import json

app = Flask(__name__)
metrics = PrometheusMetrics(app)

port_number=os.environ['MONGO_SERVER_PORT']
#connect to MongoDB Server
client = MongoClient(host='db_menu', port=27019, username='menu', password='12345')
#switch to db FatboyEat
db = client.FatboyEat

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

# Return a JSON object with all attributes of all menu sort by menu_id                  
@app.route ('/menus', methods=['GET'])
def get_all_menu():
    menus = list(db.menu.find({},{"_id" : 0}).sort("store_id", 1))
    if len(menus) == 0:
        return jsonify({"Error":"menu not found"}), 404
    else:
        return jsonify((menus)), 200

#/menus: Return a JSON object with all the menus’ attributes of a store
@app.route ('/stores/<store_id>/menus', methods=['GET'])
def get_menu(store_id):
    menus = list(db.menu.find({"store_id": store_id},{"_id" : 0}).sort("dishes_id", 1))
    if len(menus) == 0:
        return jsonify({"Error":"menu not found"}), 404
    else:
        return jsonify((menus)), 200

# create or update the entire menu for a specific store.
@app.route ('/stores/<store_id>/menus', methods=['POST'])
def update_menu(store_id):
    try:
        #convert json data from request body to python dict
        data = request.json
        check_record_exist=((db.menu.find(data).count())!=0) & (data["store_id"] == store_id)
        if (check_record_exist==True):
            return f"This record is already existed",409
        else:
            dbResponse = db.menu.insert_one(data)
            return jsonify({"message":"Menu of the following store added", "store_id":f"{store_id}"}),201
    except:
        return jsonify({"message":"sorry cannot add the menu of this store", "store_id":f"{store_id}"}),500
    
# updates an individual item within a menu.
@app.route ('/stores/<store_id>/menus/dishes/<dishes_id>', methods=['POST'])
def update_item(store_id, dishes_id):
    try:
        #convert json data from request body to python dict
        data = request.json
        check_record_exist=((db.menu.find(data).count())!=0) & (data["store_id"] == store_id)
        if (check_record_exist==True):
            return f"This record is already existed",409
        else:
            old_dishes = db.menu.find_one({"store_id": store_id, "dishes_id": dishes_id},{"_id" : 0})
            new_dishes = {"$set": request.json}
            db.menu.update_one(old_dishes, new_dishes)
            return jsonify({"update": "success"}),200
    except:
        return jsonify({"message":"sorry cannot update the menu of this store", "store_id":f"{store_id}", "dishes_id":f"{dishes_id}"}),500
    
# Delete an individual item within a menu.
@app.route ('/stores/<store_id>/menus/dishes/<dishes_id>', methods=['DELETE'])
def delete_item(store_id, dishes_id):
    try:
        if (db['menu'].count_documents({"store_id": store_id,'dishes_id':dishes_id}) > 0):
            db['menu'].delete_one({"store_id": store_id,'dishes_id':dishes_id})
            return jsonify({'store_id': store_id,'dishes_id':dishes_id, 'stage':"Removed"}), 200
        else:
            return jsonify(message="Cannot find the dish in the menu"), 404
    except:
        return jsonify({"message":"sorry cannot remove this dish of this store", "DishID":f"{dishes_id}"}),500

if __name__ == "__main__":
    #this Python flask REST API listen at port 15000 at 0.0.0.0 within the container.
    app.run(host='0.0.0.0', port=15000)