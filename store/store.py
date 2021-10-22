import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
import json

app = Flask(__name__)

port_number=os.environ['MONGO_SERVER_PORT']
#connect to MongoDB Server
client = MongoClient(host='db_store', port=27017, username='store', password='12345')
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


if __name__ == "__main__":
    #this Python flask REST API listen at port 15002 at 0.0.0.0 within the container.
    app.run(host='0.0.0.0', port=15002, debug=True)