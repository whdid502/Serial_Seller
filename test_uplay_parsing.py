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
        game_original_price = game.select_one('div > div > div > div > div > span > span.price-item').get_text(" ", strip=True).replace('₩','',1)
        game_discount_rate = game.select_one('div > div > div > div > div > div.deal-percentage').get_text(" ", strip=True).translate({ ord('-'): '', ord('%'): ''})
        game_discount_price = game.select_one('div > div > div > div > div > span.price-sales').text.replace('₩','',1)
    else:
        game_original_price = game.select_one('div > div > div > div > div > span.price-sales').text.replace('₩','',1)
        game_discount_rate = 0
        game_discount_price = None
    print(game_discount_price)