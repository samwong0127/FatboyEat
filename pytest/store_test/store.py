import pytest
import requests
import json

wrong_id = "wrongID"
url = "http://localhost:20080/store"

def test_store_api():
    response = requests.get(url+"/api")
    j = json.loads(response.text)
    assert response.status_code == 200
    #print(j['API'])
    assert j['API'] == "store"

    response = requests.get(url+"/idk_what_is_this")
    #j = json.loads(response.text)
    assert response.status_code == 404

def test_get_all_store():
    response = requests.get(url+'/stores')
    j = json.loads(response.text)
    assert response.status_code == 200

def test_get_store_with_id():
    store_id = '00001'
    response = requests.get(url+'/stores/'+store_id)
    j = json.loads(response.text)
    #print((j))
    assert response.status_code == 200
    assert j[0]['store_id'] == store_id

    response = requests.get(url+'/stores/'+wrong_id)
    j = json.loads(response.text)
    assert response.status_code == 404
    assert j['Error'] == "Store not found"

def test_get_store_with_category():
    category = 'Japanese'
    response = requests.get(url+'/stores/category/'+category)
    j = json.loads(response.text)
    #print((j))
    assert response.status_code == 200
    assert j[0]['categories'] == category