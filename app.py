from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import pymongo
import requests
from bs4 import BeautifulSoup
import math
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/serial_seller', methods = ['POST', 'GET'])
def game_main_page():
   return render_template('game_sales.html')


@app.route('/sell_page')
def game_sell_page():
   return render_template('sell_page.html')

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
      result_db = intermediate_db.skip((sort_page-1)*16).limit(16)
  else:
      result_db = intermediate_db

  output=[]

  for s in result_db:
          output.append({'platform': s['platform'], 'link': s['link'], 'img': s['img'], 'title': s['title'], 'original_price': s['original_price'], 'discount_rate': s['discount_rate'], 'discount_price': s['discount_price'], 'original_price_usd': s['original_price_usd'], 'discount_price_usd': s['discount_price_usd']})
  return jsonify({'result': output})

@app.route('/all_games_info_original')
def all_games():
    url_for_page = 'https://store.steampowered.com/search/?ignore_preferences=1&page=1'
    response_for_page = requests.get(url_for_page)
    source_for_page = response_for_page.text
    soup_for_page = BeautifulSoup(source_for_page, 'html.parser')
    maximum_page_tag = soup_for_page.select_one('div.search_pagination_left').contents[0].strip()
    split_tag = maximum_page_tag.split('-')
    game_per_page = split_tag[1].split('of')[0].strip()
    maximum_game = split_tag[1].split('of')[1].strip()
    max_page = math.ceil(int(maximum_game)/int(game_per_page))
    whole_info = []
    for page_number in range(1, max_page+1):
        url = 'https://store.steampowered.com/search/?ignore_preferences=1&page=' + str(page_number)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        games = soup.select('div#search_resultsRows > a')
        for game in games:
            if game.select_one('div > div > div.search_discount > span') != None:
                game_title = 'not found'
                game_link = 'not found'
                game_original_price = 'not found'
                game_img = 'not found'

            else:
                game_title = game.select_one('div > div > span.title').text
                game_original_price = game.select_one('div > div > div.search_price').text.replace('₩', '',1).strip().replace(',','')
                game_link = game['href']
                game_img = game.select_one('div > img').get('src')
        game_dic = [{'link': game_link}, {'img': game_img}, {'title': game_title}, {'original_price': game_original_price}]
        whole_info.append(game_dic)

    output = []

    for s in whole_info:
              output.append({'link': s['link'], 'img': s['img'], 'title': s['title'], 'original_price': s['original_price']})
    return jsonify({'result': output})

@app.route('/mywish_page')
def game_mywish_page():
   return render_template('mywish_page.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)