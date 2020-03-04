from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb://13.209.3.126:27017")
db = client.dball_games

for x in db.info.find():
    print(x)