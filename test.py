from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb://13.209.3.126:27017")
db = client.dball_games

n=14

for n in range(1,100):
    test_db = db.info.find().skip(n-1).limit(8)
    print(test_db)