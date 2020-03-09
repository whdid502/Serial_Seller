from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests
import json
from bs4 import BeautifulSoup
import math

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
        client = MongoClient('localhost', 27017)
        db = client.dball_games_not_sale
        db.info.insert_one({'platform': 'steam', 'link': game_link, 'img': game_img, 'title': game_title,
                            'original_price': game_original_price, 'status' : 'not discount'})

        # return game_title, game_img, game_link, game_original_price
#     whole_info.append({{'link' :game_link}, {'img' : game_img}, {'title' : game_title}, {'original_price' : game_original_price}})
#     client
