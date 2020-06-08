import os
if os.path.exists("env.py"):
    import env
import pymongo
import os

DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"
MONGODB_URI = os.getenv("MONGO_URI")


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '12/03/1952', 'hair_color': 'grey', 'occupation': 'writer', 'nationality': 'english'}

coll.insert(new_doc)

documents = coll.find({'nationality': 'english'})

for doc in documents:
    print(doc)