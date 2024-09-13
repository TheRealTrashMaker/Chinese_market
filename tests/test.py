from Chinese_market_api.outer_api.a_stock.Ashare import *

df = get_price(code="sh010107", frequency="1m", count=200)
print(df)
