from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import pymongo
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/serial_seller', methods = ['POST', 'GET'])
def game_main_page():
   return render_template('game_sales.html')

@app.route('/all_games_info')
def get_steam_sale():
  client = pymongo.MongoClient("mongodb://13.209.3.126:27017")
  db = client.dball_games

  platform = request.args['platform']
  sort_condition = request.args['sort']
  sort_order = request.args['order']
  sort_page = request.args['page']

  if platform in ['steam', 'uplay', 'epic', 'direct', 'humble', 'gog']:
      filtered_db = db.info.find({'platform': platform})
  elif platform == 'all':
      filtered_db = db.info.find()

  if sort_order == 'asc':
      sort_order = pymongo.ASCENDING
  elif sort_order == 'dsc':
      sort_order = pymongo.DESCENDING

  if sort_condition in ['discount_price', 'discount_rate', 'orginal_price']:
      intermediate_db = filtered_db.sort(sort_condition, sort_order)
  else:
      intermediate_db = filtered_db.sort('page', pymongo.ASCENDING)


  sort_page = int(sort_page)
  if sort_page in range(1,100):
      result_db = intermediate_db.skip(sort_page-1).limit(8)
  else:
      result_db = intermediate_db

  output=[]

  for s in result_db:
      output.append(
          {'platform': s['platform'], 'link': s['link'], 'img': s['img'], 'title': s['title'], 'original_price': s['original_price'],
           'discount_rate': s['discount_rate'], 'discount_price': s['discount_price']})
  return jsonify({'result': output})
  #
  # platform_params = request.args.get('platform', platform)
  # sort_condition_params = request.args.get['sort', sort_condition]
  # sort_order_params = request.args.get['order', sort_order]




  # if sort_condition in ['discount_price', 'discount_rate']:
  #     result_db = filtered_db.sort(sort_condition, sort_order)
  # else:
  #     result_db = filtered_db.sort("page", pymongo.ASCENDING)
  # output = []
  # for s in db.info.find():
  #     output.append({'platform': s['platform'], 'img': s['img'], 'title': s['title'], 'original_price': s['original_price'],
  #                    'discount_rate': s['discount_rate'], 'discount_price': s['discount_price']})
  # return jsonify({'result' : output})


# @app.route(url)
# def get_sell_page():
#
#     return render_template('steam_page.html')


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



@app.route('/uplay_info', methods=['GET'])
def get_uplay_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgame_sales_info
  output = []
  for s in db.sale.find():
      output.append({'link': s['link'], 'img': s['img'], 'title': s['title'], 'original_price': s['original_price'],
                     'discount_rate': s['discount_rate'], 'discount_price': s['discount_price']})
  return jsonify({'result' : output})

@app.route('/epic_info', methods=['GET'])
def get_epic_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgame_sales_info
  output = []
  for s in db.sale.find():
      output.append({'link': s['link'], 'img': s['img'], 'title': s['title'], 'original_price': s['original_price'],
                     'discount_rate': s['discount_rate'], 'discount_price': s['discount_price']})
  return jsonify({'result' : output})

@app.route('/humble_info', methods=['GET'])
def get_humble_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgame_sales_info
  output = []
  for s in db.sale.find():
      output.append({'img': s['img'], 'title': s['title'], 'original_price': s['original_price'],
                     'discount_rate': s['discount_rate'], 'discount_price': s['discount_price']})
  return jsonify({'result' : output})

@app.route('/gog_info', methods=['GET'])
def get_gog_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgame_sales_info
  output = []
  for s in db.sale.find():
      output.append({'link': s['link'], 'img': s['img'], 'title': s['title'], 'original_price': s['original_price'],
                     'discount_rate': s['discount_rate'], 'discount_price': s['discount_price']})
  return jsonify({'result' : output})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)