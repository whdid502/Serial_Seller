import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get('https://store.ubi.com/kr/deals?srule=Best%20sellers&sz=12&start=0', headers = headers)

soup = BeautifulSoup(r.text, 'html.parser')
games = soup.select('ul#search-result-items > li > div:nth-child(1)')

for game in games:
    game_link = 'https://store.ubi.com' + game.select_one('a.thumb-link')['href']
    game_img = game.select_one('div.product-image > img')['data-desktop-src']
    game_title = game.select_one('div.card-details-wrapper > div.card-details > div.card-title > h2').get_text(" ", strip=True)
    game_subtitle = game.select_one('div.card-details-wrapper > div.card-details > div.card-subtitle > h3').text
    game_original_price = game.select_one('div.card-details-wrapper > div.card-details > div.card-info > div.card-price > div.product-price > span.price-standard > span').get_text(" ", strip=True)
    game_discount_rate = game.select_one('div.card-details-wrapper > div.card-details > div.card-additional-details > div.discount_timer_section > div.product-price > div').get_text(" ", strip=True)
    game_discount_price = game.select_one('div.card-details-wrapper > div.card-details > div.card-info > div.card-price > div.product-price > span.price-sales').text
    print(game_title, game_subtitle, game_discount_price)