import pymongo
# pprint module is used to print the json output in a formatted way
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["development"]
collection = db["flights"]
# following is the usage
pprint.pprint(collection.find_one())
client.close()

'''
Without the usage of pprint the output looks like
{'_id': ObjectId('602f2f86f98ef70670966a03'), 'departureAirport': 'MUC', 'arrivalAirport': 'SFO', 'aircraft': 'Airbus A380', 'distance': 12000, 'intercontinental': True}
With the usage of pprint the output looks like
{'_id': ObjectId('602f2f86f98ef70670966a03'),
 'aircraft': 'Airbus A380',
 'arrivalAirport': 'SFO',
 'departureAirport': 'MUC',
 'distance': 12000,
 'intercontinental': True}
'''