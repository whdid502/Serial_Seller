import requests
from bs4 import BeautifulSoup

whole_source = ""
for page_number in range(1, 4):
    url = 'https://directg.net/game/game_thumb.html?page=' + str(page_number)
    response = requests.get(url)
    whole_source = whole_source + response.text
soup = BeautifulSoup(whole_source, 'html.parser')
games = soup.select('div.spacer')


for game in games:
    game_link = 'https://directg.net/game' + game.select_one('div > a')['href'].replace('.','',1)
    game_img = game.select_one('div > a > img')['src']
    game_title = game.select_one('div.vm-product-descr-container-1 > a')['title']
    game_original_price = game.select_one('div.vm3pr-2 > div > div > span.PricebasePrice').text.replace('\\','')
    if game.select_one('div.vm3pr-0 > div > div.addtocart-bar > div > div') != None:
        game_discount_rate = game.select_one('div.vm3pr-0 > div > div.addtocart-bar > div > div > span').text.replace('%','')
        game_discount_price = game.select_one('div.vm3pr-2 > div > div.PricesalesPrice > span.PricesalesPrice').get_text(" ", strip=True).replace('\\','')
    else:
        game_discount_rate = 0
        game_discount_price = 0

    def get_rate(a, b):
        c = -(100 - (b / a * 100))
        return c
    get_rate(game_original_price, game_discount_price)
# print(game_original_price, game_discount_price, game_discount_rate)
