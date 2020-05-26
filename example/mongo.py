import pymongo
from instance.credential import *

conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('Hisnet')

#collection.insert_one({'id':'id', '게시판' : '...', '과제' : '...'})
#collection.update({'id' : 'id'},{"$set" :{"pw":"pw"} })
#re = collection.find_one({"id" : "h"},{"_id": False,"pw": True})
#notice = collection.find_one({"id" : "loveetls"},{"_id":False,"과제":True})
#check1 = collection.find_one({'id' : 'loveetls'}, {"_id":False,"pw":True})
#check2 = collection.find_one({'id' : LOGIN_ID}, {"_id":False,"과제":True})
#if check1 != ilist:
#collection.update({'chat_id': '1166940643'}, {"$set":{'Hi':'True'}})
#collection.update({'id' :'dreamjane921'}, {"$set":{"게시판":'32004'}})
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
home = collection.find_one({"id" : "dreamjane921"}, {"_id":False,"과제":True})
for i in home['과제']:
	print(i)

results = collection.find()
#collection.drop()
#collection.remove({})
#print(notice)
#re = show collection

#[print(results) for results in results]
#print(check1)
