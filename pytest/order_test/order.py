import pytest
import requests
import json

wrong_id = "wrongID"
url = "http://localhost:20080/order"

def test_order_api():
    #url = url_order()
    response = requests.get(url+"/api")
    j = json.loads(response.text)
    assert response.status_code == 200
    #print(j['API'])
    assert j['API'] == "order"

    response = requests.get(url+"/idk_what_is_this")
    #j = json.loads(response.text)
    assert response.status_code == 404

def test_get_order():
    #url = url_order()
    response = requests.get(url+"/orders/00001/list")
    j = json.loads(response.text)
    assert response.status_code == 200
    assert j[0]['order_id'] == "00001"

    response = requests.get(url+"/orders/"+wrong_id+"/list")
    j = json.loads(response.text)
    assert  j["error"]== "not found"

def test_order_addOrder():
    store_id = '00001'
    #url = url_order()
    response = requests.get(url+'/orders/'+store_id+'/addorder')
    j = json.loads(response.text)
    # Expected output: {'order_id':order_id, 'stage':"success"}
    assert j['stage'] == 'success'
    global order_id_temp 
    order_id_temp = j['order_id']

    # Test with a wrong store_id
    response = requests.get(url+'/orders/'+wrong_id+'/addorder')
    j = json.loads(response.text)
    assert j['message'] == "Please check Store ID"

def test_order_shoplist():
    #url = url_order()
    response = requests.get(url+'/orders/shoplist')
    #j = json.loads(response.text)
    assert response.status_code == 200

def test_order_removeOrder():
    order_id = order_id_temp
    #url = url_order()
    response = requests.get(url+'/orders/'+order_id+'/remove')
    j = json.loads(response.text)
    assert j['stage'] == 'Removed'

    response = requests.get(url+'/orders/'+order_id+'/remove')
    j = json.loads(response.text)
    assert j['message'] =="Cannot find the order"

    response = requests.get(url+'/orders/'+wrong_id+'/remove')
    j = json.loads(response.text)
    assert j['message'] =="Cannot find the order"    

