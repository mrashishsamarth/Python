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

"""
Output
{'_id': ObjectId('602f2f86f98ef70670966a03'), 'departureAirport': 'MUC', 'arrivalAirport': 'SFO', 'aircraft': 'Airbus A380', 'distance': 12000, 'intercontinental': True}

Note:
1. The output is not printed in pretty format
"""