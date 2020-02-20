import requests
import json

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
    game_title = game['slug']
    game_img = 'http:' + game['image'] + '_product_tile_256.jpg'
    game_original_price = game['price']['baseAmount']
    game_discount_rate = game['price']['discountPercentage']
    game_discount_price = game['price']['amount']
    print(game_title, game_original_price, game_discount_rate, game_discount_price)
