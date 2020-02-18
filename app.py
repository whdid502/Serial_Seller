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
   return render_template('game_sales.html')

@app.route('/page_steam')
def game_steam_page():
   return render_template('steam_page.html')

@app.route('/steam_info', methods=['GET'])
def get_steam_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgaemsalesinfo
  output = []
  for s in db.sale.find():
    output.append({'steam_link' : s['steam_link'], 'steam_img': s['steam_img'], 'steam_title' : s['steam_title'], 'steam_original_price' : s['steam_original_price'], 'steam_discount_rate' : s['steam_discount_rate'] , 'steam_discount_price' : s['steam_discount_price']})
  return jsonify({'result' : output})

@app.route('/steam_info', methods=['POST'])
def steam_sale():
    whole_source = ""
    for page_number in range(0, 3):
        url = 'https://store.steampowered.com/search/?specials=1&filter=topsellers&page=' + str(page_number)
        response = requests.get(url)
        whole_source = whole_source + response.text
    soup = BeautifulSoup(whole_source, 'html.parser')
    games = soup.select('div#search_resultsRows > a')
    for game in games:
        game_link = game['href']
        game_img = game.select_one('div.search_capsule > img').get('src')
        game_title = game.select_one('div.responsive_search_name_combined >  div.col.search_name.ellipsis > span').text
        game_original_price = game.select_one('div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow > span > strike').text
        game_discount_rate = game.select_one('div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_discount.responsive_secondrow > span').text
        combined_price = game.select_one('div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow')
        unwanted_price = combined_price.find('span')
        unwanted_price.extract()
        client = MongoClient('localhost', 27017)
        db = client.dbgamesalesinfo
        db.info.update({'title': game_title}, {'platform': 'steam', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': combined_price}, upsert=True)
        db.info.update({'title': game_title}, {'platform': 'steam', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': combined_price})
        for a in db.info.find():
            if {a['title'] : { "$eq": game_title }} == 0:
                db.info.remove(a['title'])
        return jsonify({'result': 'success'})

@app.route('/uplay_info', methods=['GET'])
def get_uplay_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgamesalesinfo
  output = []
  for s in db.sale.find():
    output.append({'uplay_link' : s['uplay_link'], 'uplay_img': s['uplay_img'], 'uplay_title' : s['uplay_title'], 'uplay_original_price' : s['uplay_original_price'], 'uplay_discount_rate' : s['uplay_discount_rate'] , 'uplay_discount_price' : s['uplay_discount_price']})
  return jsonify({'result' : output})

@app.route('/uplay_info', methods=['POST'])
def uplay_sale():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    r = requests.get('https://store.ubi.com/kr/deals?srule=Best%20sellers&sz=12&start=0', headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    games = soup.select('ul#search-result-items > li > div:nth-child(1)')
    for game in games:
        game_link = 'https://store.ubi.com' + game.select_one('a.thumb-link')['href']
        game_img = game.select_one('div.product-image > img')['data-desktop-src']
        game_title = game.select_one('div.card-details-wrapper > div.card-details > div.card-title > h2').get_text(" ",strip=True)
        game_subtitle = game.select_one('div.card-details-wrapper > div.card-details > div.card-subtitle > h3').text
        game_original_price = game.select_one('div.card-details-wrapper > div.card-details > div.card-info > div.card-price > div.product-price > span.price-standard > span').get_text(" ", strip=True)
        game_discount_rate = game.select_one('div.card-details-wrapper > div.card-details > div.card-additional-details > div.discount_timer_section > div.product-price > div').get_text(" ", strip=True)
        game_discount_price = game.select_one('div.card-details-wrapper > div.card-details > div.card-info > div.card-price > div.product-price > span.price-sales').text
        client = MongoClient('localhost', 27017)
        db = client.dbsteaminfo
        db.info.update({'title': game_title + ' ' + game_subtitle}, {'platform': 'uplay', 'link': game_link, 'img': game_img, 'title': game_title + ' ' + game_subtitle, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price}, upsert=True)
        db.info.update({'title': game_title + ' ' + game_subtitle}, {'platform': 'uplay', 'link': game_link, 'img': game_img, 'title': game_title + ' ' + game_subtitle, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
        for a in db.info.find():
            if {a['title'] : { "$eq": game_title + ' ' + game_subtitle }} == 0:
                db.info.remove(a['title'])
        return jsonify({'result': 'success'})

@app.route('/epic_info', methods=['GET'])
def get_epic_sale():
  client = MongoClient('localhost', 27017)
  db = client.dbgamesalesinfo
  output = []
  for s in db.sale.find():
    output.append({'epic_link' : s['epic_link'], 'epic_img': s['epic_img'], 'epic_title' : s['epic_title'], 'epic_original_price' : s['epic_original_price'], 'epic_discount_rate' : s['epic_discount_rate'] , 'epic_discount_price' : s['epic_discount_price']})
  return jsonify({'result' : output})

@app.route('/epic_info', methods=['POST'])
def epic_sale():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    r = requests.get('https://www.epicgames.com/store/ko/collection/for-the-love-of-the-games', headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    games = soup.select('div.BrowseGrid-cardsContainer_4f87230c > div > a')
    for game in games:
        game_link = 'https://www.epicgames.com' + game['href']
        game_img = game.select_one('div > div > div > div > div.Picture-picture_6dd45462 > img')['data-image']
        game_title = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > span.OfferTitleInfo-title_abc02a91').text
        game_original_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > s').text
        game_discount_rate = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > span.PurchaseTag-tag_9dafbeea').text
        game_discount_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > span').text
        client = MongoClient('localhost', 27017)
        db = client.dbsteaminfo
        db.info.update({'title': game_title}, {'platform': 'epic', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price}, upsert=True)
        db.info.update({'title': game_title}, {'platform': 'epic', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
        for a in db.info.find():
            if {a['title'] : { "$eq": game_title }} == 0:
                db.info.remove(a['title'])
        return jsonify({'result': 'success'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)