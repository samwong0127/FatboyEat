db.auth('menu', '12345')
db = db.getSiblingDB('fakeUberEat')

db.createCollection('menu');

db.menu.insertOne({'store_id':'00001', 'store_name':'Sushiro HK', 'dishes_name': 'Sushi A', 'price': '10'});
db.menu.insertOne({'store_id':'00001', 'store_name':'Sushiro HK', 'dishes_name': 'Sushi B', 'price': '20'});
db.menu.insertOne({'store_id':'00001', 'store_name':'Sushiro HK', 'dishes_name': 'Sushi C', 'price': '30'});

db.menu.insertOne({'store_id':'00002', 'store_name':'TamJai Yunnan Mixian', 'dishes_name': 'Mixian B', 'price': '35'});
db.menu.insertOne({'store_id':'00003', 'store_name':'Pizza Hut', 'dishes_name': 'Pizza C', 'price': '128'});
