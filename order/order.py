import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from prometheus_flask_exporter import PrometheusMetrics
import json

app = Flask(__name__)
metrics = PrometheusMetrics(app)

#connect to MongoDB Server
client = MongoClient(host='db_order', port=27018, username='order', password='12345')
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
    return jsonify({"API":"order"}), 200

@app.route ('/orders', methods=['GET'])
def order():
    #The orders sorted in ascending order of order ID.
    orders =list(db.order.find({},{"_id" : 0}).sort("order_id", 1))
    if len(orders) == 0:
        return jsonify({"Error":"order not found"}), 404
    else:
        return jsonify((orders)), 200

#/orders: Return a JSON object with all the orders’ attributes of a orderID
@app.route ('/orders/<order_id>/list', methods=['GET'])
def each_order(order_id):
    orders = list(db.order.find({"order_id": order_id},{"_id" : 0}))
    if len(orders) == 0:
        return jsonify({"Error":"order not found"}), 404
    else:
        return jsonify((orders)), 200

@app.route ('/orders/shoplist', methods=['GET'])
def shop_list():
    orders = list(db.store_list.find({},{"_id" : 0}))
    if len(orders) == 0:
        return jsonify({"Error":"order not found"}), 404
    else:
        return jsonify((orders)), 200

@app.route ('/orders/<order_id>/remove', methods=['DELETE'])
def Remove_order(order_id):
    try:
        dbResponse = db.order.delete_one({"order_id": order_id})
        if dbResponse.deleted_count==1:
            return jsonify({"message":"order deleted", "order_id":f"{order_id}"}),200
        else:
            return jsonify({"message":"order not found", "order_id":f"{order_id}"}),404
    except:
        return jsonify({"message":"sorry cannot delete order"}),500

### Endpoint below may need to change
@app.route ('/orders/<storeID>/addorder')
def add_order(storeID):
    order_id = "00001"
    while (db["order"].count_documents({"order_id": order_id}) > 0):
        order_id = '{:05d}'.format(int(order_id) + 1)

    if (db["store_list"].count_documents({"store_id": storeID}) == 1):
        store = db['store_list'].find_one({"store_id": storeID})
        store_name = str(store['store_name'])
        db['order'].insert_one({'order_id': order_id, 'store_id': storeID, 'store_name': store_name, 'customer_id': '11111'})
        return jsonify({'order_id':order_id, 'stage':"success"})
    else:
        return jsonify(message="Please check Store ID")

if __name__ == "__main__":
    #this Python flask REST API listen at port 15001 at 0.0.0.0 within the container.
    app.run(host='0.0.0.0', port=15001)
