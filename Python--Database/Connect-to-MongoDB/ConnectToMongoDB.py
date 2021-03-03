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

"""
The output looks like the following

{'_id': ObjectId('602f2f86f98ef70670966a03'),
 'aircraft': 'Airbus A380',
 'arrivalAirport': 'SFO',
 'departureAirport': 'MUC',
 'distance': 12000,
 'intercontinental': True}

{'_id': ObjectId('602f2f86f98ef70670966a04'),
 'aircraft': 'Airbus A320',
 'arrivalAirport': 'TXL',
 'departureAirport': 'LHR',
 'distance': 950,
 'intercontinental': False}


Process finished with exit code 0
"""