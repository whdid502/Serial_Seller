from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbtestgame

data1 = {'platform': 'steam', 'link': 'http://naver.com', 'img': 'https://cdn.pixabay.com/photo/2015/06/10/06/11/library-804498_960_720.jpg', 'title': '디비전2', 'original_price': '50000', 'discount_rate': '50', 'discount_price': '25000'}

db.test.insert_one(data1)