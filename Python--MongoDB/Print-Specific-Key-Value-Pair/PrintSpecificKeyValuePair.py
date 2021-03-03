import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["development"]
collection = db["flights"]

for item in collection.find():
    pprint.pprint("aircraft is :- " + item["aircraft"])
    print()

client.close()

'''
-----------------------------------------------------------------------
Output with - pprint.pprint(item)
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
-----------------------------------------------------------------------
Output with pprint.pprint("aircraft" + item["aircraft"])
'aircraft is :- Airbus A380'
'aircraft is :- Airbus A320'
'''
