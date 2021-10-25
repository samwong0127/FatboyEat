import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
import json

app = Flask(__name__)

port_number=os.environ['MONGO_SERVER_PORT']
#connect to MongoDB Server
client = MongoClient(host=os.environ['MONGO_SERVER_HOST'], port=int(port_number), username=os.environ['MONGO_USERNAME'], password=os.environ['MONGO_PASSWORD'])
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
    return jsonify({"group_number": "5", "group_members":[{"Name": "Wong Pan Chi", "Student_ID": "18063466D"},{"Name": "Wong Kin Sang", "Student_ID": "18051915D"},{"Name": "Yuen Chun Ming", "Student_ID": "18059819D"},{"Name": "Sin Kwo Yin", "Student_ID": "18059048D"}]), 200

#/stores: Return a JSON object with all the stores’ attributes
@app.route ('/stores', methods=['GET'])
def store():
    #The stores sorted in ascending order of store ID.
    stores =db.store.find({},{"_id" : 0}).sort("store_id", 1)
    result = []
    for store in stores:
        temp = {}
        for key, value in store.items():
            if (type(store[key])==str):
                temp[key] = str(store[key])
            else:
                temp[key] = store[key]
        result.append(temp)
    return jsonify(result),200



                    

if __name__ == "__main__":
    #this Python flask REST API listen at port 15000 at 0.0.0.0 within the container.
    app.run(host='0.0.0.0', port=15000, debug=True)
