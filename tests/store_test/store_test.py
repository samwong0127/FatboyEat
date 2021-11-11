import pytest
import requests
import json

wrong_id = "wrongID"
url = "http://localhost:20080/store"
headers = {
    'Content-Type':'application/json',
    'Accept':'*/*',
    'Connection':'keep-alive'
}

def test_store_api():
    response = requests.get(url+"/api")
    j = json.loads(response.text)
    assert response.status_code == 200
    assert j['API'] == "store"
    
def test_store_api_Err404():
    response = requests.get(url+"/idk_what_is_this")
    assert response.status_code == 404

def test_get_all_stores():
    response = requests.get(url+'/stores')
    j = json.loads(response.text)
    assert response.status_code == 200

def test_get_store_with_id():
    store_id = '00001'
    response = requests.get(url+'/stores/'+store_id)
    j = json.loads(response.text)
    assert response.status_code == 200
    assert j[0]['store_id'] == store_id

# Get a store with a wrong store id
def test_get_store_with_id_Err404():
    response = requests.get(url+'/stores/'+wrong_id)
    j = json.loads(response.text)
    assert response.status_code == 404
    assert j['Error'] == "Store not found"

# Get all stores with the same category
def test_get_store_with_category():
    category = 'Japanese'
    response = requests.get(url+'/stores/category/'+category)
    j = json.loads(response.text)
    assert response.status_code == 200
    assert j[0]['categories'] == category

# Get all stores with a non-existing category
def test_get_store_with_category_Err404():
    category = 'NoSuchCategory'
    response = requests.get(url+'/stores/category/'+category)
    j = json.loads(response.text)
    assert response.status_code == 404
    
