import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get('https://www.epicgames.com/store/ko/browse?sortBy=effectiveDate&sortDir=DESC&pageSize=1000', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
games = soup.select('div.BrowseGrid-card_9f6a50fb')
# <div class="BrowseGrid-card_9f6a50fb"><a aria-label="35/205, Cardpocalypse, Gambrinous | Versus Evil, 17500" href="/store/ko/product/cardpocalypse/home"><div class="OfferCard-root_9eb0888e"><div class="OfferCard-content_2b8b08c0"><div class="OfferCard-imageWrapper_dee193c9"><div class="OfferCardImagePortrait-container_93d6ce17" data-testid="offer-card-image-portrait"><div class="Picture-picture_6dd45462"><img src="https://cdn1.epicgames.com/epic/offer/Cardpocalypse_MainGame_EpicGamesStore_S3_Store_Portrait_ApprovedPublic_v2%20(1)-1280x1440-ecb2dc25cc10ada5474a6537d8eb9e63.jpg?h=854&amp;resize=1&amp;w=640" alt="" data-image="https://cdn1.epicgames.com/epic/offer/Cardpocalypse_MainGame_EpicGamesStore_S3_Store_Portrait_ApprovedPublic_v2%20(1)-1280x1440-ecb2dc25cc10ada5474a6537d8eb9e63.jpg?h=854&amp;resize=1&amp;w=640" class="Picture-image_c7ea350b OfferCardImageArt-picture_2bc1f4cf OfferCardImagePortrait-picture_96fce0b8 Picture-visible_5e20a43f"></div><div class="OfferCardImageLogo-container_2b04e712"><div class="DynamicLogo-wrapper_6fb5bed4 DynamicLogo-smallContainer_c0a44c51 undefined"><img class="DynamicLogo-logo_3af88135" src="https://cdn1.epicgames.com/epic/offer/Cardpocalypse_Logo-WithLight-1843x659-3386ddc5eb8023b982b17ff53fd56275.png?h=270&amp;resize=1&amp;w=480" alt="Cardpocalypse"></div></div></div></div><div class="OfferCard-meta_34c2e3a1"><span data-testid="offer-title-info-title" class="OfferTitleInfo-title_abc02a91">Cardpocalypse</span><span data-testid="offer-title-info-subtitle" class="OfferTitleInfo-subtitle_ad134671">Gambrinous | Versus Evil</span><div class="PurchasePrice-price_ca0dc1d8"><span class="DiscountAmount-hiddenScreenReader_b98454d9">-30% 할인 중</span><span class="PurchaseTag-tag_452447bf">-30%</span><div class="PurchasePrice-priceContainer_f0baeac9"><s class="Price-discount_01260a89">₩25,000</s><span class="Price-original_a6834d25">₩17,500</span></div></div></div></div></div></a></div>
print(games)
for game in games:
    if game.select_one('a > div > div > div > div > span') != None:
        game_link = 'https://www.epicgames.com' + game.select_one('a')['href']
        # print(game_link)
        game_img = game.select_one('a > div > div > div > div > div > img')['src']
        game_title = game.select_one('a > div > div > div > span').text
        game_original_price = game.select_one('a > div > div > div > div > div > s').text.translate(
            {ord('₩'): '', ord(','): ''}).strip()
        game_discount_price = game.select_one('a > div > div > div > div > div > span').text.translate(
            {ord('₩'): '', ord(','): ''}).strip()
        game_discount_rate = game.select_one('a > div > div > div > div > span.PurchaseTag-tag_452447bf').text.translate(
            {ord('-'): '', ord('%'): ''})
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
    else:
        continue

    # print(game_link)

    # print(game_original_price)
    # game_original_price = game_original_price.replace(',','')
    # game_discount_price = game_discount_price.replace(',','')
    # print(game_original_price, game_discount_price)
    # def get_rate():
    #     discount_rate = 100 - (float(game_discount_price) / float(game_original_price) * 100)
    #     return float(discount_rate)
    # print(game_discount_rate, get_rate())