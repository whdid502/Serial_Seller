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
    game_img = game.select_one('div > img').get('src')
    game_title = game.select_one('div > div > span.title').text
    game_original_price = game.select_one('div > div > div > span > strike').text.replace('₩','',1).strip().replace(',','')
    game_discount_rate = game.select_one('div > div > div > span').text.translate({ ord('-'): '', ord('%'): ''})
    combined_div = game.select_one('div > div > div.search_price')
    unwanted_div = game.select_one('div > div > div.search_price > span')
    for div in unwanted_div:
        div.extract()
    game_discount_price = combined_div.text.replace('₩','',1).strip().replace(',','')
    print(game_title, game_original_price, game_discount_rate, game_discount_price)

    # def get_rate():
    #     discount_rate = 100 - (float(game_discount_price) / float(game_original_price) * 100)
    #     return float(discount_rate)
    # print(game_discount_rate, '/', get_rate())