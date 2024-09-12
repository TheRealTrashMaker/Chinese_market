import json
import re
import time
import requests


def get_kline_by_minutes(symbol, minutes):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": f"https://finance.sina.com.cn/futures/quotes/{symbol}.shtml",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = f"https://stock2.finance.sina.com.cn/futures/api/jsonp.php/var%20_{symbol}_{minutes}_{time.time() * 1000}=/InnerFuturesNewService.getFewMinLine"
    params = {
        "symbol": symbol,
        "type": minutes
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        unclean_data = re.findall("\((.*)\)", response.text)[0]
        return json.loads(unclean_data)
    except:
        return None


if __name__ == "__main__":
    print(get_kline_by_minutes("TA2501", "5"))
