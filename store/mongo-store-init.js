db.auth('store', '12345')
db = db.getSiblingDB('fakeUberEat')

db.createCollection('store');

db.store.insertOne({'store_id':'00001', 'store_name':'Sushiro HK', 'phone_number':'26698317', 'categories':'Japanese', 'location':'Shop G10, G/F, Deli Place (Site 4), The Whampoa, Hung Hom', 'opening hour':'10:30 - 22:30'});
db.store.insertOne({'store_id':'00002', 'store_name':'TamJai Yunnan Mixian', 'phone_number':'22781813', 'categories':'Chinese', 'location':'Shop No. G35, G/F, Site 11, Whampoa Garden, Hunghom, Kowloon', 'opening hour':'07:30 - 21:45'});
db.store.insertOne({'store_id':'00003', 'store_name':'Pizza Hut', 'phone_number':'2764 5490', 'categories':'Italian', 'location':'Shop G10A, G/F, Site 2, Whampoa Gdn, Hunghom', 'opening hour':'11:00 - 22:30'});
