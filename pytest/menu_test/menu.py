import pytest
import requests
import json

wrong_id = "wrongID"
url = "http://localhost:20080/menu"

def test_menu_api():
    response = requests.get(url+"/api")
    j = json.loads(response.text)
    assert response.status_code == 200
    #print(j['API'])
    assert j['API'] == "menu"

    response = requests.get(url+"/idk_what_is_this")
    #j = json.loads(response.text)
    assert response.status_code == 404

def test_get_menu():
    store_id = '00001'
    response = requests.get(url+"/stores/"+store_id+"/menus")
    j = json.loads(response.text)
    assert response.status_code == 200
    #print(j)
    
    response = requests.get(url+"/stores/"+wrong_id+"/menus")
    j = json.loads(response.text)
    assert  j["error"]== "not found"

def test_update_menu():
    data = {"store_id": "33", "store_name": "AAA", "dishes_name": "sushi abc", "price": "100"}
    r = requests.post(url+'/stores/33/menus', data=json.dumps(data))
    #print(r)
    response = requests.get(url+"/stores/33/menus")
    j = json.loads(response.text)
    print(j)
    assert response.status_code == 200
    assert j['store_id'] == store_id   
    # NOT YET FINISHED

def test_update_within_menu():
    
    assert "Will be done later" == "When?" 