import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get('https://www.epicgames.com/store/ko/collection/ubisoft-sale', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
games = soup.select('div.BrowseGrid-cardsContainer_4f87230c > div > a')

for game in games:
    game_link = 'https://www.epicgames.com' + game['href']
    game_img = game.select_one('div > div > div > div > div.Picture-picture_6dd45462 > img')['data-image']
    game_title = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > span.OfferTitleInfo-title_abc02a91').text
    if game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > span') != None:
        game_original_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > s').text.translate(
            {ord('₩'): '', ord(','): ''}).strip()
        game_discount_rate = game.select_one(
            'div > div > div.OfferCard-meta_34c2e3a1 > div > span.PurchaseTag-tag_452447bf').text.translate(
            {ord('-'): '', ord('%'): ''})
        game_discount_price = game.select_one(
            'div > div > div.OfferCard-meta_34c2e3a1 > div > div > span').text.translate(
            {ord('₩'): '', ord(','): ''}).strip()
    else:
        game_discount_rate = 0
        game_original_price = game.select_one(
            'div > div > div.OfferCard-meta_34c2e3a1 > div > div > span').text.translate(
            {ord('₩'): '', ord(','): ''}).strip()
        game_discount_price = game_original_price
    game_discount_price = int(game_discount_price)
    game_discount_rate = int(game_discount_rate)
    game_original_price = int(game_original_price)
    def upbit_get_usd_krw():
        url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
        exchange = requests.get(url).json()
        return exchange[0]['basePrice']


    krw = upbit_get_usd_krw()
    game_original_price_usd = round(game_original_price / krw, 2)
    game_discount_price_usd = round(game_discount_price / krw, 2)
    print(game_title, game_original_price, game_original_price_usd, game_discount_rate, game_discount_price, game_discount_price_usd)

    # print(game_original_price)
    # game_original_price = game_original_price.replace(',','')
    # game_discount_price = game_discount_price.replace(',','')
    # print(game_original_price, game_discount_price)
    # def get_rate():
    #     discount_rate = 100 - (float(game_discount_price) / float(game_original_price) * 100)
    #     return float(discount_rate)
    # print(game_discount_rate, get_rate())