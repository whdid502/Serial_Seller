import requests
import json

url1 = 'https://www.g2a.com/new/api/v2/products/filter?category_id=trending-products-c1663&currency=KRW&store=korean&variant_category=1663&wholesale=false'
games_1st = requests.get(url1).text
print(games_1st)
# games_1st_dic = json.loads(games_1st)
# url2 = 'https://www.g2a.com/new/api/v2/products/filter?category_id=trending-products-c1663&changeType=PAGINATION&currency=KRW&page=2&store=korean&variant_category=1663&wholesale=false'
# games_2nd = requests.get(url2).text
# games_2nd_dic = json.loads(games_2nd)
#
# games_1st_value = games_1st_dic.setdefault('products')
# games_2nd_value = games_2nd_dic.setdefault('products')
#
# games = games_1st_value + games_2nd_value
#
# for game in games:
#     game_title = game['name']
#     game_img = game['image']['sources']['url']
#     game_original_price = game['full_price']['amount']
#     game_discount_price = game['current_price']['amount']
#     print(game_title)

# G2A는 접근권한이 없어서 크롤링, api 둘다안됨