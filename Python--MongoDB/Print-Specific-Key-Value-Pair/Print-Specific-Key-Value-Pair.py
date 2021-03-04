import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["development"]
collection = db["flights"]

for item in collection.find():
    pprint.pprint("aircraft is :- " + item["aircraft"])
    print()

client.close()