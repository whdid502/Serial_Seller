import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get('https://www.epicgames.com/store/ko/collection/for-the-love-of-the-games', headers = headers)

soup = BeautifulSoup(r.text, 'html.parser')
games = soup.select('div.BrowseGrid-cardsContainer_4f87230c > div > a')

for game in games:
    game_link = 'https://www.epicgames.com' + game['href']
    game_img = game.select_one('div > div > div > div > div.Picture-picture_6dd45462 > img')['data-image']
    game_title = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > span.OfferTitleInfo-title_abc02a91').text
    game_original_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > s').text.replace('₩','',1)
    game_discount_rate = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > span.PurchaseTag-tag_9dafbeea').text.translate({ ord('-'): '', ord('%'): ''})
    game_discount_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > span').text.replace('₩','',1)
    print(game_title, game_original_price, game_discount_price, game_discount_rate)