db.auth('order', '12345')
db = db.getSiblingDB('fakeUberEat')

db.createCollection('order');

db.order.insertOne({'order_id':'00001','store_id':'00001', 'store_name':'Sushiro HK', 'customer_id':'00123'});
db.order.insertOne({'order_id':'00002','store_id':'00002', 'store_name':'TamJai Yunnan Mixian', 'customer_id':'00456'});
db.order.insertOne({'order_id':'00003','store_id':'00003', 'store_name':'Pizza Hut', 'customer_id':'00789'});

db.createCollection('store_list');
db.store_list.insertOne({'store_id':'00001', 'store_name':'Sushiro HK'});
db.store_list.insertOne({'store_id':'00002', 'store_name':'TamJai Yunnan Mixian'});
db.store_list.insertOne({'store_id':'00003', 'store_name':'Pizza Hut'});
