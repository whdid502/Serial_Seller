from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/serial_seller')
def game_main_page():
    # paradict = {'platform':platform, }
   return render_template('game_sales.html')

url = '/sell_page'
@app.route(url)
def get_sell_page():
    return render_template('steam_page.html')


@app.route('/sell_page')
def game_sell_page():
   return render_template('sell_page.html')

@app.route('/epic_page')
def game_epic_page():
   return render_template('epic_page.html')

@app.route('/uplay_page')
def game_uplay_page():
   return render_template('uplay_page.html')

@app.route('/humble_page')
def game_humble_page():
   return render_template('humble_page.html')

@app.route('/gog_page')
def game_gog_page():
   return render_template('gog_page.html')

@app.route('/directgames_page')
def game_directgames_page():
   return render_template('directgames_page.html')

@app.route('/discount_rate_page')
def game_discount_rate_page():
   return render_template('discount_rate_page.html')

@app.route('/discount_price_page')
def game_discount_price_page():
   return render_template('discount_price_page.html')

@app.route('/mywish_page')
def game_mywish_page():
   return render_template('mywish_page.html')

@app.route('/steam_info', methods=['GET'])
def get_steam_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgaemsalesinfo
  output = []
  for s in db.sale.find():
    output.append({'steam_link' : s['steam_link'], 'steam_img': s['steam_img'], 'steam_title' : s['steam_title'], 'steam_original_price' : s['steam_original_price'], 'steam_discount_rate' : s['steam_discount_rate'] , 'steam_discount_price' : s['steam_discount_price']})
  return jsonify({'result' : output})

@app.route('/uplay_info', methods=['GET'])
def get_uplay_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgamesalesinfo
  output = []
  for s in db.sale.find():
    output.append({'uplay_link' : s['uplay_link'], 'uplay_img': s['uplay_img'], 'uplay_title' : s['uplay_title'], 'uplay_original_price' : s['uplay_original_price'], 'uplay_discount_rate' : s['uplay_discount_rate'] , 'uplay_discount_price' : s['uplay_discount_price']})
  return jsonify({'result' : output})

@app.route('/epic_info', methods=['GET'])
def get_epic_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgamesalesinfo
  output = []
  for s in db.sale.find():
    output.append({'epic_link' : s['epic_link'], 'epic_img': s['epic_img'], 'epic_title' : s['epic_title'], 'epic_original_price' : s['epic_original_price'], 'epic_discount_rate' : s['epic_discount_rate'] , 'epic_discount_price' : s['epic_discount_price']})
  return jsonify({'result' : output})

@app.route('/humble_info', methods=['GET'])
def get_humble_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgamesalesinfo
  output = []
  for s in db.sale.find():
    output.append({'humble_img': s['humble_img'], 'humble_title' : s['humble_title'], 'humble_original_price' : s['humble_original_price'], 'humble_discount_price' : s['humble_discount_price']})
  return jsonify({'result' : output})

@app.route('/gog_info', methods=['GET'])
def get_gog_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgamesalesinfo
  output = []
  for s in db.sale.find():
    output.append({'epic_link' : s['epic_link'], 'epic_img': s['epic_img'], 'epic_title' : s['epic_title'], 'epic_original_price' : s['epic_original_price'], 'epic_discount_rate' : s['epic_discount_rate'] , 'epic_discount_price' : s['epic_discount_price']})
  return jsonify({'result' : output})

@app.route('/test_info', methods=['GET'])
def test_db():
  client = MongoClient('localhost', 27017)
  db = client.dbtestgame
  output = []
  for s in db.test.find():
    output.append({'test_link' : s['link'], 'test_img': s['img'], 'test_title' : s['title'], 'test_original_price' : s['original_price'], 'test_discount_rate' : s['discount_rate'] , 'test_discount_price' : s['discount_price']})
  return jsonify({'result' : output})

@app.route('/test_info2', methods=['GET'])
def test2_db():
  client = MongoClient('localhost', 27017)
  db = client.dbtestgame2
  output = []
  for s in db.test.find():
    output.append({'test_link' : s['link'], 'test_img': s['img'], 'test_title' : s['title'], 'test_original_price' : s['original_price'], 'test_discount_rate' : s['discount_rate'] , 'test_discount_price' : s['discount_price']})
  return jsonify({'result' : output})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)