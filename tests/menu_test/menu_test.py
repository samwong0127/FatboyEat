
import pytest
import requests
import json

wrong_id = "wrongID"
url = "http://localhost:20080/menu"
headers = {
    'Content-Type':'application/json',
    'Accept':'*/*',
    'Connection':'keep-alive'
}
def test_menu_api():
    response = requests.get(url+"/api")
    j = json.loads(response.text)
    assert response.status_code == 200
    #print(j['API'])
    assert j['API'] == "menu"

def test_menu_api_Err404():
    response = requests.get(url+"/idk_what_is_this")
    #j = json.loads(response.text)
    assert response.status_code == 404

def test_get_all_menu():
    #store_id = '00001'
    response = requests.get(url+"/menus", headers=headers)
    #j = json.loads(response.text)
    assert response.status_code == 200
    #print(j)
    

def test_get_menu():
    store_id = '00001'
    response = requests.get(url+"/stores/"+store_id+"/menus", headers=headers)
    #j = json.loads(response.text)
    assert response.status_code == 200
    #print(j)
    
def test_get_menu_Err404():
    response = requests.get(url+"/stores/"+wrong_id+"/menus", headers=headers)
    #j = json.loads(response.text)
    assert response.status_code == 404
    #assert  j["error"]== "not found"

# {'store_id':'00001', 'store_name':'Sushiro HK', 'dishes_id':'1', 'dishes_name': 'Sushi A', 'price': '10'}
def test_update_menu():
    data = {"store_id": "33", "store_name": "AAA", 'dishes_id':'1', "dishes_name": "sushi abc", "price": "100"}
    response = requests.post(url+'/stores/33/menus', data=json.dumps(data), headers=headers)
    #print(r)
    j = json.loads(response.text)
    assert response.status_code == 201
    assert j['store_id'] == '33'
    # NOT YET FINISHED

def test_update_menu_Err409():
    data = {"store_id": "33", "store_name": "AAA", 'dishes_id':'1', "dishes_name": "sushi abc", "price": "100"}
    response = requests.post(url+'/stores/33/menus', data=json.dumps(data), headers=headers)
    #j = json.loads(response.text)
    #print(j)
    assert response.status_code == 409
    
def test_update_menu_Err500():
    data2 = {"store_id": "33", "store_name": "AAA", "dishes_name": "sushi abc"}
    response = requests.post(url+'/stores/33/menus', data=json.dumps(data2))
    #print(j)
    assert response.status_code == 500



def test_update_menu_item():
    data2 = {"store_id": "33", "store_name": "AAA", 'dishes_id':'1', "dishes_name": "sushi def", "price": "120"}
    response = requests.post(url+'/stores/33/menus/dishes/1', data=json.dumps(data2), headers=headers)
    #print(j)
    assert response.status_code == 200


def test_update_menu_item_Err409():
    data2 = {"store_id": "33", "store_name": "AAA", 'dishes_id':'1', "dishes_name": "sushi def", "price": "120"}
    response = requests.post(url+'/stores/33/menus/dishes/1', data=json.dumps(data2), headers=headers)
    #print(j)
    assert response.status_code == 409

def test_update_menu_item_Err500():
    data2 = {"store_id": "33", "store_name": "AAA", "dishes_name": "sushi def", "price":"130"}
    response = requests.post(url+'/stores/33/menus/dishes/1', data=json.dumps(data2))
    #print(j)
    assert response.status_code == 500