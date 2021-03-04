# pymongo module must be imported for Python to connect to MongoDB
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
# sample database - "development"
db = client["development"]
# sample collection - "flights"
collection = db["flights"]
# print one random document from the collection utilized
print(collection.find_one())
client.close()