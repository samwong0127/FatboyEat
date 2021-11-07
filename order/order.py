import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from prometheus_flask_exporter import PrometheusMetrics
import json

app = Flask(__name__)
metrics = PrometheusMetrics(app)

#connect to MongoDB Server
client = MongoClient(host='db_order', port=27018, username='order', password='12345')
client2 = MongoClient(host='db_store', port=27017, username='store', password='12345')
#switch to db fakeUberEat
db = client.fakeUberEat
storedb = client2.fakeUberEat

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

# Return the API using
@app.route ('/api', methods=['GET'])
def whereami():
    return jsonify({"API":"order"}), 200


#/orders: Return a JSON object with all the orders’ attributes
@app.route ('/orders/<orderID>/list', methods=['GET'])
def each_order(orderID):
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
    #db = connect_order_db()
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

@app.route ('/addorder/stores/<storeID>', methods=['POST'])
def add_order(storeID):
    order_id = "00001"
    try:
        data = request.json
        while (db["order"].count_documents({"order_id": order_id}) > 0):
            order_id = '{:05d}'.format(int(order_id) + 1)

        if (storedb["store"].count_documents({"store_id": storeID}) > 0):
            # data.append({"order_id": order_id})
            data["order_id"] = order_id
            db['order'].insert_one(data)
            return jsonify({'store_id':storeID, 'order_id':order_id, 'stage':"success"}), 201
        else:
            return jsonify({"message":"Please check Store ID", "store_id":f"{storeID}"}), 404
        data.append({"order_id": order_id})
        # db['order'].insert_one(data)
        # return jsonify({'store_id':storeID, 'order_id':order_id, 'stage':"success"}), 201
    except:
        return jsonify({"message":"sorry cannot add order of this store", "store_id":f"{storeID}"}),500

@app.route ('/deleteorder/orders/<OrderID>', methods=['DELETE'])
def Remove_order(OrderID):
    #db = connect_order_db()
    try:
        if (db['order'].count_documents({"order_id": OrderID}) > 0):
            db['order'].delete_one({"order_id": OrderID})
            return jsonify({'order_id':OrderID, 'stage':"Removed"}), 201
        else:
            return jsonify(message="Cannot find the order"), 404
    except:
        return jsonify({"message":"sorry cannot remove order of this store", "OrderID":f"{OrderID}"}),500

if __name__ == "__main__":
    #this Python flask REST API listen at port 15001 at 0.0.0.0 within the container.
    app.run(host='0.0.0.0', port=15001)
