import pymongo
collection = pymongo.MongoClient("mongodb://localhost:27017").development.flights
print(collection.find_one())