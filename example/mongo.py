import pymongo
from instance.credential import *


conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('customer')


results = collection.find()
#ollection.remove({})

[print(results) for results in results]
