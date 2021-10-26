import pytest
from unit import *
import requests
from flask import Flask, jsonify, request
from pymongo import MongoClient
import json

def test_add():
    assert add(3,4)==7

def test_sub():
    assert sub(3,4)==-1

def test_order_api():
    response = requests.get(url_order()+"/api")
    j = json.loads(response.text)
    assert response.status_code == 200
    #print(j['API'])
    assert j['API'] == "order"

def test_order_returningAttribute():
    url = url_order()+"/orders/00001/list"
    response = requests.get(url)
    j = json.loads(response.text)
    assert response.status_code == 200
    assert j[0]['order_id'] == "00001"

'''
def test_order_addOrder():
    store_id = '00001'
    #order_id = "00001"
    url = url_order()+'/orders/'+store_id+'/addorder'
    response = requests.get(url)
    j = json.loads(response.text)
    # {'order_id':order_id, 'stage':"success"}
    assert j['stage'] == 'success'
    assert j['order_id'] == '00001'
'''
    
