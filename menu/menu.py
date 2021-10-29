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
                if (key == "dishes_id" or key == "dishes_name" or key == "price"):
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
@app.route ('/stores/<store_id>/menus', methods=['POST'])
def update_menu(store_id):
    # menu = db['menu'].find({"store_id": store_id})
    data = request.get_json(force=True)
        # {"store_id": store_id,"store_name": "AAA","dishes_name": "sushi abc","price": "100"},
        # {"store_id": store_id,"store_name": "BBB","dishes_name": "sushi abcd","price": "200"}

    try:
        db['menu'].insert_many(data)
        # db['menu'].update_one(
        #     {"store_id": store_id},
        #     {
        #         "$set": {
        #             "store_name": "dawdaw" ,
        #             "dishes_name": "sushi abc",
        #             "price": "100"
        #         }
        #     }
        # )
    except Exception as e:
        print(e)
    update_data = db['menu'].find({"store_id": store_id},{"_id" : 0})
    output = []
    for item in update_data:
        output.append(item)
    
    return jsonify(output), 200

# updates an individual item within a menu.
@app.route ('/stores/<store_id>/menus/dishes/<dishes_id>', methods=['POST'])
def update_item(store_id, dishes_id):
    dishes = db['menu'].find({"store_id": store_id, "dishes_id": dishes_id},{"_id" : 0})

    temp=[]
    for item in dishes:
        temp.append(item)
    # return jsonify(temp),200
    old_dishes = {"dishes_name": temp[0]['dishes_name'], "price": temp[0]['price']}
    new_dishes = request.get_json(force=True)
    # new_dishes = {"$set": { "dishes_name": "new_dishes", "price": "1000" }}
    
    db['menu'].update_one(old_dishes, new_dishes)

    return jsonify({"update": "success"}),200
    
if __name__ == "__main__":
    #this Python flask REST API listen at port 15000 at 0.0.0.0 within the container.
    app.run(host='0.0.0.0', port=15000)