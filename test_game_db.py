from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests
import json
from bs4 import BeautifulSoup

def upbit_get_usd_krw():
    url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
    exchange = requests.get(url).json()
    return exchange[0]['basePrice']
usd = upbit_get_usd_krw()

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
        game_img = game.select_one('div > img').get('src')
        game_title = game.select_one('div > div > span.title').text
        game_original_price = game.select_one('div > div > div > span > strike').text.replace('₩', '',1).strip().replace(',','')
        game_discount_rate = game.select_one('div > div > div > span').text.translate({ord('-'): '', ord('%'): ''})
        combined_div = game.select_one('div > div > div.search_price')
        unwanted_div = game.select_one('div > div > div.search_price > span')
        for div in unwanted_div:
            div.extract()
        game_discount_price = combined_div.text.replace('₩', '', 1).strip().replace(',', '')
        game_original_price = int(game_original_price)
        game_discount_rate = int(game_discount_rate)
        game_discount_price = int(game_discount_price)
        client = MongoClient('localhost', 27017)
        db = client.dball_games
        # db.info.update_many({'title': game_title}, {'platform': 'steam', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price}, upsert=True)
        # db.info.update_many({'title': game_title}, {'platform': 'steam', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
        # for a in db.info.find():
        #     if {a['title'] : { "$eq": game_title }} == 0:
        #         db.info.remove(a['title'])
        db.info.insert_one({'platform': 'steam', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate,'discount_price': game_discount_price})
        # print({'platform': 'steam', 'link': game_link, 'img': game_img, 'title': game_title,
        #  'original_price': game_original_price, 'discount_rate': game_discount_rate,
        #  'discount_price': game_discount_price})
steam_sale()
                
def uplay_sale():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    r = requests.get('https://store.ubi.com/kr/deals?srule=Best%20sellers&sz=12&start=0', headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    games = soup.select('ul#search-result-items > li > div:nth-child(1)')
    for game in games:
        game_link = 'https://store.ubi.com' + game.select_one('a.thumb-link')['href']
        game_img = game.select_one('div.product-image > img')['data-desktop-src']
        game_title = game.select_one('div > div > div > h2.prod-title').get_text(" ",strip=True) + ' ' + game.select_one('div > div > div > h3').text
        if game.select_one('div > div > div > div > div > div.deal-percentage') != None:
            game_original_price = game.select_one('div > div > div > div > div > span > span.price-item').text.translate({ord('₩'): '', ord(','): ''}).strip()
            game_discount_rate = game.select_one('div > div > div > div > div > div.deal-percentage').text.translate({ord('-'): '', ord('%'): ''}).strip()
            game_discount_price = game.select_one('div > div > div > div > div > span.price-sales').text.translate({ord('₩'): '', ord(','): ''}).strip()
        else:
            game_original_price = game.select_one('div > div > div > div > div > span.price-sales').text.translate({ord('₩'): '', ord(','): ''}).strip()
            game_discount_rate = 0
            game_discount_price = game_original_price
        game_original_price = int(game_original_price)
        game_discount_rate = int(game_discount_rate)
        game_discount_price = int(game_discount_price)
        client = MongoClient('localhost', 27017)
        db = client.dball_games
        # db.info.update_many({'title': game_title}, {'platform': 'uplay', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price}, upsert=True)
        # db.info.update_many({'title': game_title}, {'platform': 'uplay', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
        # for a in db.info.find():
        #     if {a['title'] : { "$eq": game_title }} == 0:
        #         db.info.remove(a['title'])
        db.info.insert_one({'platform': 'uplay', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
uplay_sale()

def epic_sale():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    r = requests.get('https://www.epicgames.com/store/ko/collection/ubisoft-sale', headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    games = soup.select('div.BrowseGrid-cardsContainer_4f87230c > div > a')
    for game in games:
        game_link = 'https://www.epicgames.com' + game['href']
        game_img = game.select_one('div > div > div > div > div.Picture-picture_6dd45462 > img')['data-image']
        game_title = game.select_one(
            'div > div > div.OfferCard-meta_34c2e3a1 > span.OfferTitleInfo-title_abc02a91').text
        if game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > span') != None:
            game_original_price = game.select_one(
                'div > div > div.OfferCard-meta_34c2e3a1 > div > div > s').text.translate(
                {ord('₩'): '', ord(','): ''}).strip()
            game_discount_rate = game.select_one(
                'div > div > div.OfferCard-meta_34c2e3a1 > div > span.PurchaseTag-tag_452447bf').text.translate(
                {ord('-'): '', ord('%'): ''})
            game_discount_price = game.select_one(
                'div > div > div.OfferCard-meta_34c2e3a1 > div > div > span').text.translate(
                {ord('₩'): '', ord(','): ''}).strip()
        else:
            game_discount_rate = 0
            game_original_price = game.select_one(
                'div > div > div.OfferCard-meta_34c2e3a1 > div > div > span').text.translate(
                {ord('₩'): '', ord(','): ''}).strip()
            game_discount_price = game_original_price
        game_discount_price = int(game_discount_price)
        game_discount_rate = int(game_discount_rate)
        game_original_price = int(game_original_price)
        client = MongoClient('localhost', 27017)
        db = client.dball_games
        # db.info.update_many({'title': game_title}, {'platform': 'epic', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price}, upsert=True)
        # db.info.update_many({'title': game_title}, {'platform': 'epic', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
        # for a in db.info.find():
        #     if {a['title'] : { "$eq": game_title }} == 0:
        #         db.info.remove(a['title'])
        db.info.insert_one({'platform': 'epic', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
epic_sale()

def humble_sale():
    url1 = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=0'
    games_1st = requests.get(url1).text
    games_1st_dic = json.loads(games_1st)
    url2 = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=1'
    games_2nd = requests.get(url2).text
    games_2nd_dic = json.loads(games_2nd)
    url3 = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=2'
    games_3rd = requests.get(url3).text
    games_3rd_dic = json.loads(games_3rd)
    url4 = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=3'
    games_4th = requests.get(url4).text
    games_4th_dic = json.loads(games_4th)
    games_1st_value = games_1st_dic.setdefault('results')
    games_2nd_value = games_2nd_dic.setdefault('results')
    games_3rd_value = games_3rd_dic.setdefault('results')
    games_4th_value = games_4th_dic.setdefault('results')
    games = games_1st_value + games_2nd_value + games_3rd_value + games_4th_value
    for game in games:
        game_title = game['human_name']
        game_img = game['standard_carousel_image']
        game_original_price_usd = game['full_price']['amount']
        game_link = 'https://www.humblebundle.com/store/search?sort=discount&filter=onsale&hmb_source=store_navbar'
        game_discount_price_usd = game['current_price']['amount']

        def upbit_get_usd_krw():
            url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
            exchange = requests.get(url).json()
            return exchange[0]['basePrice']

        krw = upbit_get_usd_krw()
        game_original_price = round(game_original_price_usd * krw)
        game_discount_price = round(game_discount_price_usd * krw)
        game_discount_rate = round((game_original_price_usd - game_discount_price_usd) / game_original_price_usd * 100)
        client = MongoClient('localhost', 27017)
        db = client.dball_games
        # db.info.update_many({'title': game_title}, {'platform': 'humblebundle', 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price}, upsert=True)
        # db.info.update_many({'title': game_title}, {'platform': 'humblebundle', 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
        # for a in db.info.find():
        #     if {a['title'] : { "$eq": game_title }} == 0:
        #         db.info.remove(a['title'])
        db.info.insert_one({'platform': 'humble', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price, 'original_price_usd' : game_original_price_usd, 'discount_price_usd' : game_discount_price_usd})
humble_sale()

def gog_sale():
    url1 = 'https://www.gog.com/games/ajax/filtered?mediaType=game&page=1&price=discounted&sort=popularity'
    games_1st = requests.get(url1).text
    games_1st_dic = json.loads(games_1st)
    url2 = 'https://www.gog.com/games/ajax/filtered?mediaType=game&page=1&price=discounted&sort=popularity'
    games_2nd = requests.get(url2).text
    games_2nd_dic = json.loads(games_2nd)
    games_1st_value = games_1st_dic.setdefault('products')
    games_2nd_value = games_2nd_dic.setdefault('products')
    games = games_1st_value + games_2nd_value
    for game in games:
        game_link = 'https://www.gog.com/' + game['url']
        game_title = game['title']
        game_img = 'http:' + game['image'] + '_product_tile_256.jpg'
        game_original_price_usd = game['price']['baseAmount']
        game_discount_rate = game['price']['discountPercentage']
        game_discount_price_usd = game['price']['finalAmount']
        game_discount_price_usd = float(game_discount_price_usd)
        game_original_price_usd = float(game_original_price_usd)

        def upbit_get_usd_krw():
            url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
            exchange = requests.get(url).json()
            return exchange[0]['basePrice']

        krw = upbit_get_usd_krw()
        game_discount_price = round(game_discount_price_usd * krw)
        game_original_price = round(game_original_price_usd * krw)
        client = MongoClient('localhost', 27017)
        db = client.dball_games
        # db.info.update_many({'title': game_title}, {'platform': 'gog', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price}, upsert=True)
        # db.info.update_many({'title': game_title}, {'platform': 'gog', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
        # for a in db.info.find():
        #     if {a['title'] : { "$eq": game_title }} == 0:
        #         db.info.remove(a['title'])
        db.info.insert_one({'platform': 'gog', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price, 'original_price_usd' : game_original_price_usd, 'discount_price_usd' : game_discount_price_usd})
gog_sale()

def direct_sale():
    whole_source = ""
    for page_number in range(1, 4):
        url = 'https://directg.net/game/game_thumb.html?page=' + str(page_number)
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = None
        whole_source = whole_source + response.text
    soup = BeautifulSoup(whole_source, 'html.parser')
    games = soup.select('div.spacer')

    for game in games:
        game_link = 'https://directg.net/game' + game.select_one('div > a')['href'].replace('.', '', 1)
        game_img = game.select_one('div > a > img')['src']
        game_title = game.select_one('div.vm-product-descr-container-1 > a')['title']
        game_original_price = game.select_one('div.vm3pr-2 > div > div > span.PricebasePrice').text.translate(
            {ord('\\'): '', ord(','): ''}).strip()
        if game.select_one('div.vm3pr-0 > div > div.addtocart-bar > div > div') != None:
            game_discount_rate = game.select_one(
                'div.vm3pr-0 > div > div.addtocart-bar > div > div > span').text.replace(
                '%', '').strip()
            game_discount_price = game.select_one(
                'div.vm3pr-2 > div > div.PricesalesPrice > span.PricesalesPrice').text.replace('\\', '').replace(',',
                                                                                                                 '').strip()
        else:
            game_discount_rate = 0
            game_discount_price = game_original_price
        game_discount_price = int(game_discount_price)
        game_discount_rate = int(game_discount_rate)
        game_original_price = int(game_original_price)
        client = MongoClient('localhost', 27017)
        db = client.dball_games
        # db.info.update_many({'title': game_title}, {'platform': 'direct', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price}, upsert=True)
        # db.info.update_many({'title': game_title}, {'platform': 'direct', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
        # for a in db.info.find():
        #     if {a['title'] : { "$eq": game_title }} == 0:
        #         db.info.remove(a['title'])
        db.info.insert_one({'platform': 'direct', 'link': game_link, 'img': game_img, 'title': game_title, 'original_price': game_original_price, 'discount_rate': game_discount_rate, 'discount_price': game_discount_price})
direct_sale()


# client = MongoClient('localhost', 27017)
# db = client.dbgame_sales_info
# print(db.info.find({'platform'}))