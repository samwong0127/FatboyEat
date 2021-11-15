db.auth('menu', '12345')
db = db.getSiblingDB('FatboyEat')

db.createCollection('menu');

db.menu.insertOne({'store_id':'00001', 'store_name':'Sushiro HK', 'dishes_id':'00001', 'dishes_name':'Sushi A', 'price':10, 'avaliability':true});
db.menu.insertOne({'store_id':'00001', 'store_name':'Sushiro HK', 'dishes_id':'00002', 'dishes_name':'Sushi B', 'price':20, 'avaliability':false});
db.menu.insertOne({'store_id':'00001', 'store_name':'Sushiro HK', 'dishes_id':'00003', 'dishes_name':'Sushi C', 'price':30, 'avaliability':true});

db.menu.insertOne({'store_id':'00002', 'store_name':'TamJai Yunnan Mixian', 'dishes_id':'00004','dishes_name':'Mixian B', 'price':35, 'avaliability':true});
db.menu.insertOne({'store_id':'00003', 'store_name':'Pizza Hut', 'dishes_id':'00005','dishes_name':'Pizza C', 'price':128, 'avaliability':true});
