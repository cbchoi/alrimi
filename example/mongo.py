import pymongo
from instance.credential import *


conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('i')

#collection.insert_one({'id':'id', '게시판' : '...', '과제' : '...'})
#collection.update({'id' : 'id'},{"$set" :{"pw":"pw"} })
#re = collection.find_one({"id" : "h"},{"_id": False,"pw": True})
#notice = collection.find_one({"id" : "loveetls"},{"_id":False,"과제":True})
#check1 = collection.find_one({'id' : 'loveetls'}, {"_id":False,"pw":True})
#check2 = collection.find_one({'id' : LOGIN_ID}, {"_id":False,"과제":True})
#if check1 != ilist:
#collection.update({'id' :'loveetls'}, {"$unset":{"pw":True}})
#collection.update({'id' :'loveetls'}, {"$set":{"pw":'sit32004'}})
#print('ok')
'''else:
collection.update({'id' : LOGIN_ID}, {"$unset":{"게시판": check1}})
print("yes")'''

'''if check1 != ilist:
collection.update({'id' : LOGIN_ID}, {"$set":{"게시판":ilst}})
print('ok')
else:
collection.update({'id' : LOGIN_ID}, {"$unset":{"게시판": check1}})
collection.update({'id' : LOGIN_ID}, {"$set":{"게시판": ilst}})
print("yes")'''


results = collection.find()
#collection.remove({})
#print(notice)
#re = show collection

[print(results) for results in results]
#print(check1)
