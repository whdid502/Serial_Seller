from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbtest_def
def insertone():
    db.info.insert_one({'name': '조양권', 'age':28})
insertone()