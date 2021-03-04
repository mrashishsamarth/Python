import pymongo
# pprint module is used to print the json output in a formatted way
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["development"]
collection = db["flights"]
# following is the usage
pprint.pprint(collection.find_one())
client.close()

