import requests
from bs4 import BeautifulSoup

whole_source = ""
for page_number in range(0, 3):
    url = 'https://store.steampowered.com/search/?specials=1&filter=topsellers&page=' + str(page_number)
    response = requests.get(url)
    whole_source = whole_source + response.text
soup = BeautifulSoup(whole_source, 'html.parser')
games = soup.select('div#search_resultsRows > a')

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
# r = requests.get('https://store.steampowered.com/search/?specials=1&filter=topsellers', headers = headers)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# games = soup.select('div#search_resultsRows > a')
# print(games)
for game in games:
    game_link = game['href']
    game_img = game.select_one('div.search_capsule > img').get('src')
    game_title = game.select_one('div.responsive_search_name_combined >  div.col.search_name.ellipsis > span').text
    game_original_pirce = game.select_one('div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow > span > strike').text
    game_discount_rate = game.select_one('div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_discount.responsive_secondrow > span').text
    combined_price = game.select_one('div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow')
    unwanted_price = combined_price.find('span')
    unwanted_price.extract()
    print(game_title, combined_price)