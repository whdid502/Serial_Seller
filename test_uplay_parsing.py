import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get('https://store.ubi.com/kr/deals?srule=Best%20sellers&sz=12&start=0', headers = headers)

soup = BeautifulSoup(r.text, 'html.parser')
games = soup.select('ul#search-result-items > li > div')

for game in games:
    game_link = 'https://store.ubi.com' + game.select_one('a.thumb-link')['href']
    game_img = game.select_one('div.product-image > img')['data-desktop-src']
    game_title = game.select_one('div > div > div > h2.prod-title').get_text(" ", strip=True) + ' ' + game.select_one('div > div > div > h3').text
    if game.select_one('div > div > div > div > div > div.deal-percentage') != None:
        game_original_price = game.select_one('div > div > div > div > div > span > span.price-item').text.translate({ ord('₩'): '', ord(','): ''}).strip()
        game_discount_rate = game.select_one('div > div > div > div > div > div.deal-percentage').text.translate({ ord('-'): '', ord('%'): ''}).strip()
        game_discount_price = game.select_one('div > div > div > div > div > span.price-sales').text.translate({ ord('₩'): '', ord(','): ''}).strip()
    else:
        game_original_price = game.select_one('div > div > div > div > div > span.price-sales').text.translate({ ord('₩'): '', ord(','): ''}).strip()
        game_discount_rate = 0
        game_discount_price = game_original_price


    print(game_title, game_original_price, game_discount_rate, game_discount_price)

    #
    # def get_rate():
    #     discount_rate = 100 - (float(game_discount_price) / float(game_original_price) * 100)
    #     return float(discount_rate)
    # print(game_discount_rate, '/', get_rate())