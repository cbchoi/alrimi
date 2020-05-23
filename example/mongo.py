import pymongo
from instance.credential import *


conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('i')

#collection.insert_one({'id':'id', '게시판' : '...', '과제' : '...'})
#collection.update({'id' : 'id'},{"$set" :{"pw":"pw"} })
#re = collection.find_one({"id" : "h"},{"_id": False,"pw": True})
#notice = collection.find_one({"id" : "loveetls"},{"_id":False,"과제":True})
results = collection.find()
#collection.remove({})
#print(notice)
#re = show collection

#[print(results) for results in results]
#print(collection)
