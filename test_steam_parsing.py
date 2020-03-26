import requests
from bs4 import BeautifulSoup
import json

whole_source = ""
for page_number in range(1, 4):
    url = 'https://store.steampowered.com/search/?specials=1&filter=topsellers&page=' + str(page_number)
    response = requests.get(url)
    whole_source += response.text
soup = BeautifulSoup(whole_source, 'html.parser')
games = soup.select('div#search_resultsRows > a')
print(games)
games_info = []
def steam_sale():
    whole_source = ""
    for page_number in range(1, 4):
        url = 'https://store.steampowered.com/search/?specials=1&filter=topsellers&page=' + str(page_number)
        response = requests.get(url)
        whole_source = whole_source + response.text
    soup = BeautifulSoup(whole_source, 'html.parser')
    games = soup.select('div#search_resultsRows > a')
    for game in games:
        game_link = game['href']
        game_img = game.select_one('div > img').get('src')
        game_title = game.select_one('div > div > span.title').text
        game_original_price = game.select_one('div > div > div > span > strike').text.replace('₩', '',
                                                                                              1).strip().replace(
            ',', '')
        game_discount_rate = game.select_one('div > div > div > span').text.translate({ord('-'): '', ord('%'): ''})
        combined_div = game.select_one('div > div > div.search_price')
        unwanted_div = game.select_one('div > div > div.search_price > span')
        for div in unwanted_div:
            div.extract()
        game_discount_price = combined_div.text.replace('₩', '', 1).strip().replace(',', '')
        game_original_price = int(game_original_price)
        game_discount_rate = int(game_discount_rate)
        game_discount_price = int(game_discount_price)

        def upbit_get_usd_krw():
            url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
            exchange = requests.get(url).json()
            return exchange[0]['basePrice']

        krw = upbit_get_usd_krw()
        game_original_price_usd = round(game_original_price / krw, 2)
        game_discount_price_usd = round(game_discount_price / krw, 2)
        game = {'platform' : 'steam', 'link' : game_link ,'img' : game_img, 'title' : game_title, 'original_price' : game_discount_price, "discount_rate" : game_discount_rate, 'discount_price' : game_discount_price, 'original_price_usd' : game_original_price_usd, 'discount_price_usd' : game_discount_price_usd}
        games_info.append(game)
# steam_sale()

# def uplay_sale():
#     headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
#     r = requests.get('https://store.ubi.com/kr/deals?srule=Best%20sellers&sz=12&start=1', headers = headers)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     games = soup.select('ul#search-result-items > li > div:nth-child(1)')
#     for game in games:
#         game_link = 'https://store.ubi.com' + game.select_one('a.thumb-link')['href']
#         game_img = game.select_one('div.product-image > img')['data-desktop-src']
#         game_title = game.select_one('div > div > div > h2.prod-title').get_text(" ",
#                                                                                  strip=True) + ' ' + game.select_one(
#             'div > div > div > h3').text
#         if game.select_one('div > div > div > div > div > div.deal-percentage') != None:
#             game_original_price = game.select_one(
#                 'div > div > div > div > div > span > span.price-item').text.translate(
#                 {ord('₩'): '', ord(','): ''}).strip()
#             game_discount_rate = game.select_one('div > div > div > div > div > div.deal-percentage').text.translate(
#                 {ord('-'): '', ord('%'): ''}).strip()
#             game_discount_price = game.select_one('div > div > div > div > div > span.price-sales').text.translate(
#                 {ord('₩'): '', ord(','): ''}).strip()
#         else:
#             game_original_price = game.select_one('div > div > div > div > div > span.price-sales').text.translate(
#                 {ord('₩'): '', ord(','): ''}).strip()
#             game_discount_rate = 0
#             game_discount_price = game_original_price
#
#         def upbit_get_usd_krw():
#             url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
#             exchange = requests.get(url).json()
#             return exchange[0]['basePrice']
#
#         krw = upbit_get_usd_krw()
#         game_original_price = int(game_original_price)
#         game_discount_rate = int(game_discount_rate)
#         game_discount_price = int(game_discount_price)
#         game_original_price_usd = round(game_original_price / krw, 2)
#         game_discount_price_usd = round(game_discount_price / krw, 2)
#     game = {'platform': 'uplay', 'link': game_link, 'img': game_img, 'title': game_title,
#             'original_price': game_discount_price, "discount_rate": game_discount_rate,
#             'discount_price': game_discount_price, 'original_price_usd': game_original_price_usd,
#             'discount_price_usd': game_discount_price_usd}
#     games_info.append(game)
# uplay_sale()
#
# print(games_info)
    # def get_rate():
    #     discount_rate = 100 - (float(game_discount_price) / float(game_original_price) * 100)
    #     return float(discount_rate)
    # print(game_discount_rate, '/', get_rate())