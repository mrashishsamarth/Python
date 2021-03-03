import pymongo
collection = pymongo.MongoClient("mongodb://localhost:27017").development.flights
print(collection.find_one())

'''
1. This is another way (one liner) to use pymongo to connect to locally installed mongo db
2. Print a non-pretty formatted output of one randomly selected document
Output:
{'_id': ObjectId('602f2f86f98ef70670966a03'), 'departureAirport': 'MUC', 'arrivalAirport': 'SFO', 'aircraft': 'Airbus A380', 'distance': 12000, 'intercontinental': True}
'''