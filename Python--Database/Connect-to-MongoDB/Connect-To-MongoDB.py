# Import pymongo module for mongo db connection
import pymongo
# Import pprint module for pretty printing on the JSON output of the document
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
# using the "development" database
db = client["development"]
# Using the "flights" collection
collection = db["flights"]
# Executing the for loop to pretty print all the documents in the collection
for item in collection.find():
    pprint.pprint(item)
    print()
client.close()

