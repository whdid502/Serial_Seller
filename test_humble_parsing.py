import requests
from bs4 import BeautifulSoup

whole_source = ""
for page_number in range(0, 4):
    url = 'https://www.humblebundle.com/store/search?sort=bestselling&filter=onsale&hmb_source=store_navbar&page=' + str(page_number)
    response = requests.get(url)
    whole_source = whole_source + response.text
soup = BeautifulSoup(whole_source, 'html.parser')
# games = soup.select('')

print(soup)

# for game in games:
#     game_link = game.select_one('a')['href']
    # game_img = game.select_one('div > div > div > div > div.Picture-picture_6dd45462 > img')['data-image']
    # game_title = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > span.OfferTitleInfo-title_abc02a91').text
    # game_original_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > s').text
    # game_discount_rate = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > span.PurchaseTag-tag_9dafbeea').text
    # game_discount_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > span').text
    # print(game_link)