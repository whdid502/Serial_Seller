from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbtestgame2

data1 = {'platform': 'uplay', 'link': 'http://google.com', 'img': 'https://cdn.pixabay.com/photo/2015/06/10/06/11/library-804498_960_720.jpg', 'title': '레인보우식스시즈', 'original_price': '20000', 'discount_rate': '20', 'discount_price': '16000'}

db.test.insert_one(data1)