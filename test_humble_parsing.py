import requests
import json
from collections import ChainMap


# whole_source = ""
# for page_number in range(0, 4):
#     url = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=' + str(page_number)
#     response = requests.get(url)
#     whole_source = whole_source + response.text

url1 = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=0'
games_1st = requests.get(url1).text
games_1st_dic = json.loads(games_1st)
url2 = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=1'
games_2nd = requests.get(url2).text
games_2nd_dic = json.loads(games_2nd)
url3 = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=2'
games_3rd = requests.get(url3).text
games_3rd_dic = json.loads(games_3rd)
url4 = 'https://www.humblebundle.com/store/api/search?sort=bestselling&filter=onsale&request=2&page=3'
games_4th = requests.get(url4).text
games_4th_dic = json.loads(games_4th)
games_1st_value = games_1st_dic.setdefault('results')
games_2nd_value = games_2nd_dic.setdefault('results')
games_3rd_value = games_3rd_dic.setdefault('results')
games_4th_value = games_4th_dic.setdefault('results')
games = games_1st_value + games_2nd_value + games_3rd_value + games_4th_value
# print(games)
for game in games:
    game_title =
print(game_title)
# #
# print(whole_source)

# for game in games:
#     game_link =
#     game_title = game['results']['human_name']
# print(game_title)
# soup = BeautifulSoup(whole_source, 'html.parser')
# games = soup.select('li.entity-block-container js-entity-container > div > div.entity')

# print(soup)

# for game in games:
#     game_link = game.select_one('a')['href']
    # game_img = game.select_one('div > div > div > div > div.Picture-picture_6dd45462 > img')['data-image']
    # game_title = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > span.OfferTitleInfo-title_abc02a91').text
    # game_original_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > s').text
    # game_discount_rate = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > span.PurchaseTag-tag_9dafbeea').text
    # game_discount_price = game.select_one('div > div > div.OfferCard-meta_34c2e3a1 > div > div > span').text
    # _link)print(game