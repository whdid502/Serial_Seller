import requests
import json

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
    game_discount_rate = round((game_original_price_usd - game_discount_price_usd)/game_original_price_usd*100)

    print(game_title, game_original_price_usd, game_original_price, game_discount_rate, game_discount_price_usd, game_discount_price)