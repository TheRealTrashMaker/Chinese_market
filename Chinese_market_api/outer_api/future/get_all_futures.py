from tqsdk import TqApi, TqAuth

api = TqApi(auth=TqAuth("admin852", "admin852"))
quote = api.get_quote("SHFE.ni2206")

# 输出 ni2206 的最新行情时间和最新价
print(quote.datetime, quote.last_price)

# 关闭api,释放资源
api.close()