import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get('https://store.ubi.com/kr/deals?srule=Best%20sellers&sz=12&start=0', headers = headers)

soup = BeautifulSoup(r.text, 'html.parser')
games = soup.select('ul#search-result-items > li > div:nth-child(1)')

for game in games:
    game_link = 'https://store.ubi.com' + game.select_one('a.thumb-link')['href']
    game_img = game.select_one('div.product-image card-image-wrapper > img.product-image primary-image lazy card-image swapped loaded')['src']
    # game_title = game.select_one('div.product-tile card full-tile-link full-width > div.card-details-wrapper > div.card-details > div.card-title > h2').text
    # game_original_pirce = game.select_one('div.product-tile card full-tile-link full-width > div.card-details-wrapper > div.card-details > div.card-info > div.card-price > div.product-price price deal discount-shown > span.price-standard > span').text
    # game_discount_rate = game.select_one('div.product-tile card full-tile-link full-width > div.card-details-wrapper > div.card-details > div.card-additional-details card-labels-wrapper show-timer-oncard > div.discount_timer_section deal > div.product-price price deal discount-shown > div.deal-percentage card-label card-deal').text
    # game_discount_price = game.select_one('div.product-tile card full-tile-link full-width > div.card-details-wrapper > div.card-details > div.card-info > div.card-price > div.product-price price deal discount-shown > span.price-sales standard-price').text
    print(game_img)