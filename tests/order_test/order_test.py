import pytest
import requests
import json

wrong_id = "wrongID"
url = "http://localhost:20080/order"
headers = {
    'Content-Type':'application/json',
    'Accept':'*/*',
    'Connection':'keep-alive'
}
data = {'store_id':'00001'}

def test_order_api():
    #url = url_order()
    response = requests.get(url+"/api")
    j = json.loads(response.text)
    assert response.status_code == 200
    #print(j['API'])
    assert j['API'] == "order"

def test_order_api_Err404():
    response = requests.get(url+"/idk_what_is_this")
    #j = json.loads(response.text)
    assert response.status_code == 404

def test_get_order():
    #url = url_order()
    response = requests.get(url+"/orders/00001/list")
    j = json.loads(response.text)
    assert response.status_code == 200
    assert j[0]['order_id'] == "00001"

def test_get_order_Err404():
    response = requests.get(url+"/orders/"+wrong_id+"/list")
    j = json.loads(response.text)
    assert  j["error"]== "not found"

def test_get_all_orders():
    response = requests.get(url+"/orders")
    #j = json.loads(response.text)
    assert response.status_code == 200

#def  test_get_all_shops():
#    response = requests.get(url+"/orders/shoplist")
#    #j = json.loads(response.text)
#    assert response.status_code == 200

def test_order_addOrder():
    #url = url_order()
    response = requests.post(url+'/addorder/stores/00001', headers=headers, data=data)
    j = json.loads(response.text)
    assert response.status_code == 201
    global order_id_temp 
    order_id_temp = j['order_id']

def test_order_addOrder_Err404():
    # Test with a wrong store_id
    response = requests.post(url+'/addorder/stores/'+wrong_id, headers=headers, data=data)
    #j = json.loads(response.text)
    assert response.status_code == 404

def test_order_addOrder_Err500():
    response = requests.post(url+'/addorder/stores/00001', data=data)
    #j = json.loads(response.text)
    assert response.status_code == 500

def test_order_removeOrder():
    #url = url_order()
    response = requests.delete(url+'/deleteorder/orders/'+order_id_temp, headers=headers)
    assert response.status_code == 201

def test_order_removeOrder_Err404():
    response = requests.delete(url+'/deleteorder/orders/'+order_id_temp, headers=headers)
    #j = json.loads(response.text)
    assert response.status_code == 404

    response = requests.delete(url+'/deleteorder/orders/'+wrong_id, headers=headers)
    #j = json.loads(response.text)
    assert response.status_code == 404

def test_order_removeOrder_Err500():
    response = requests.delete(url+'/deleteorder/orders/'+order_id_temp)
    #j = json.loads(response.text)
    assert response.status_code == 500

