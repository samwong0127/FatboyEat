import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
import json

app = Flask(__name__)
"""
port_number=os.environ['MONGO_SERVER_PORT']
#connect to MongoDB Server
client = MongoClient(host=os.environ['MONGO_SERVER_HOST'], port=int(port_number), username=os.environ['MONGO_USERNAME'], password=os.environ['MONGO_PASSWORD'])
#switch to db fakeUberEat
db = client.fakeUberEat
"""
def connect_order_db():
    # host = os.environ['MONGO_SERVER_HOST']
    # usr = os.environ['MONGO_USERNAME']
    # pwd = os.environ['MONGO_PASSWORD']
    # port = int(os.environ['MONGO_SERVER_PORT'])

    # try if we can connect to db.
    try:
        client = MongoClient(host="db_order",
                            port=27018, 
                            username="order", 
                            password="12345",
                            serverSelectionTimeoutMS=1000)
        client.server_info()
    # print the connection error and exit.
    except Exception as e:
        print("Could not connect to server:")
        print(e)
        exit(0)

    # return db after we connected server.
    db = client["fakeUberEat"]
    return db
db = connect_order_db()

def output(result):
    if not bool(result):
        errormsg = {'error': 'not found'}
        return jsonify(errormsg), 404
    else:
        return jsonify(result)

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

#/orders: Return a JSON object with all the orders’ attributes
@app.route ('/orders/<orderID>/list', methods=['GET'])
def each_order(orderID):
    #The orders sorted in ascending order of order ID.
    db = connect_order_db()
    orders =db['order'].find({"order_id": orderID},{"_id" : 0})
    result = []
    for order in orders:
        temp = {}
        for key in order.keys():
            if (type(order[key]) != str):
                temp[key] = order[key]
            else:
                temp[key] = str(order[key])

        result.append(temp)

    return output(result)

@app.route ('/orders', methods=['GET'])
def order():
    #The orders sorted in ascending order of order ID.
    db = connect_order_db()
    orders =db['order'].find({},{"_id" : 0}).sort("order_id", 1)
    result = []
    for order in orders:
        temp = {}
        for key in order.keys():
            if (type(order[key]) != str):
                temp[key] = order[key]
            else:
                temp[key] = str(order[key])

        result.append(temp)

    return output(result)

@app.route ('/orders/shoplist', methods=['GET'])
def shop_list():
    db = connect_order_db()
    orders =db['store_list'].find({},{"_id" : 0})
    result = []
    for order in orders:
        temp = {}
        for key in order.keys():
            if (type(order[key]) != str):
                temp[key] = order[key]
            else:
                temp[key] = str(order[key])

        result.append(temp)

    return output(result)

@app.route ('/orders/<storeID>/addorder')
def add_order(storeID):
    db = connect_order_db()
    order_id = "00001"
    while (db["order"].count_documents({"order_id": order_id}) > 0):
        order_id = '{:05d}'.format(int(order_id) + 1)
        #print("order id = ", order_id)

    if (db["store_list"].count_documents({"store_id": storeID}) == 1):
        store = db['store_list'].find_one({"store_id": storeID})
        store_name = str(store['store_name'])

        
        db['order'].insert_one({'order_id': order_id, 'store_id': storeID, 'store_name': store_name, 'customer_id': '11111'})
        return jsonify({'order_id':order_id, 'stage':"success"})
    else:
        return jsonify(message="Please check Store ID")

if __name__ == "__main__":
    #this Python flask REST API listen at port 15001 at 0.0.0.0 within the container.
    client = connect_order_db()
    app.run(host='0.0.0.0', port=15001, debug=True)