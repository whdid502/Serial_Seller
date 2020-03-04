from bs4 import BeautifulSoup
import requests

whole_source = ""
for page_number in range(1, 4):
    url = 'https://directg.net/game/game_thumb.html?page=' + str(page_number)
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = None
    whole_source = whole_source + response.text
soup = BeautifulSoup(whole_source, 'html.parser')
games = soup.select('div.spacer')

for game in games:
    game_link = 'https://directg.net/game' + game.select_one('div > a')['href'].replace('.', '', 1)
    game_img = game.select_one('div > a > img')['src']
    game_title = game.select_one('div.vm-product-descr-container-1 > a')['title']
    game_original_price = game.select_one('div.vm3pr-2 > div > div > span.PricebasePrice').text.translate(
        {ord('\\'): '', ord(','): ''}).strip()
    if game.select_one('div.vm3pr-0 > div > div.addtocart-bar > div > div') != None:
        game_discount_rate = game.select_one('div.vm3pr-0 > div > div.addtocart-bar > div > div > span').text.replace(
            '%', '').strip()
        game_discount_price = game.select_one(
            'div.vm3pr-2 > div > div.PricesalesPrice > span.PricesalesPrice').text.replace('\\', '').replace(',',
                                                                                                             '').strip()
    else:
        game_discount_rate = 0
        game_discount_price = game_original_price
    game_discount_price = int(game_discount_price)
    game_discount_rate = int(game_discount_rate)
    game_original_price = int(game_original_price)
    # print(game_title)
    print(game_title, game_original_price, game_discount_rate, game_discount_price)
    # game_original_price = float(game_original_price.replace(',',''))translate({ ord('₩'): '', ord(','): ''})
    # game_discount_price = float(game_discount_price)

    # def get_rate():
    #     discount_rate = 100 - (float(game_discount_price) / float(game_original_price) * 100)
    #     return float(discount_rate)
    # print(game_discount_rate, get_rate())
# get_rate(game_original_price, game_discount_price)
# print(game_original_price, game_discount_price, game_discount_rate)
