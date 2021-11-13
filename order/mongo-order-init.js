db.auth('order', '12345')
db = db.getSiblingDB('FatboyEat')

db.createCollection('order');

db.order.insertOne({'order_id':'00001','store_id':'00001', 'store_name':'Sushiro HK', 'customer_id':'00123', 'status':'created', 'totalprice':40, 'dishlist':[{"dish_id":"00001", "dishname":"Sushi A", "dish_price":10, "store_id":"00001"},{"dish_id":"00003", "dishname":"Sushi C", "dish_price":30, "store_id":"00003"}]});
db.order.insertOne({'order_id':'00002','store_id':'00002', 'store_name':'TamJai Yunnan Mixian', 'customer_id':'00456', 'status':'accepted', 'totalprice':35, 'dishlist':[{"dish_id":"00004", "dishname":"Mixian B", "dish_price":35, "store_id":"00002"}]});
db.order.insertOne({'order_id':'00003','store_id':'00003', 'store_name':'Pizza Hut', 'customer_id':'00789', 'status':'canceled', 'totalprice':128, 'dishlist':[{"dish_id":"00005", "dishname":"Pizza C", "dish_price":128, "store_id":"00003"}]});

// db.createCollection('store_list');
// db.store_list.insertOne({'store_id':'00001', 'store_name':'Sushiro HK'});
// db.store_list.insertOne({'store_id':'00002', 'store_name':'TamJai Yunnan Mixian'});
// db.store_list.insertOne({'store_id':'00003', 'store_name':'Pizza Hut'});
