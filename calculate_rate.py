def get_rate():
    discount_rate = 100 - (float(game_discount_price) / game_original_price * 100)
    return float(discount_rate)



#a는 원가 b는 할인가