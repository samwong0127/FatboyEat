import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from prometheus_flask_exporter import PrometheusMetrics
import json

app = Flask(__name__)
metrics = PrometheusMetrics(app)

port_number=os.environ['MONGO_SERVER_PORT']
#connect to MongoDB Server
client = MongoClient(host='db_store', port=27017, username='store', password='12345')
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
    return jsonify({"API":"store"}), 200

# Return a JSON object with all attributes of all store sort by store_id                  
@app.route ('/stores', methods=['GET'])
def get_store():
    stores = list(db.store.find({},{"_id" : 0}).sort("store_id", 1))
    if len(stores) == 0:
        return jsonify({"Error":"Store not found"}), 404
    else:
        return jsonify((stores)), 200

# Return a JSON object with all attributes of a specific store                    
@app.route ('/stores/<store_id>', methods=['GET'])
def get_store_with_id(store_id):
    stores = list(db.store.find({"store_id":store_id}, {"_id":0}))
    if len(stores) == 0:
        return jsonify({"Error":"Store not found"}), 404
    else:
        return jsonify((stores)), 200

# Return a JSON object with all attributes of a store with a specific category                    
@app.route ('/stores/category/<categories>', methods=['GET'])
def get_store_with_category(categories):
    stores = list(db.store.find({"categories":categories}, {"_id":0}))
    if len(stores) == 0:
        return jsonify({"Error":"No such category"}), 404
    else:
        return jsonify(stores), 200




                    

if __name__ == "__main__":
    #this Python flask REST API listen at port 15002 at 0.0.0.0 within the container.
    app.run(host='0.0.0.0', port=15002)

