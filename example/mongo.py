import pymongo
from instance.credential import *


conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('customer')

collection.insert_one({'id':LOGIN_ID, 'pw':LOGIN_PW})

results = collection.find()

#[print(i)]


'''if i == True:
	print("hi")
else: 
	print("wow")'''

[print(results) for results in results]

#collection.remove({})

#[print(result) for result in results]