import json
import os.path
import re
import time
from datetime import datetime

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
        return_data = []
        for item in json.loads(unclean_data):
            date_time_obj = datetime.strptime(item["d"], '%Y-%m-%d %H:%M:%S')
            # 将datetime对象转换为十位数时间戳
            timestamp = int(date_time_obj.timestamp())
            return_data.append({
                "O": item["o"],
                "C": item["c"],
                "H": item["h"],
                "L": item["l"],
                "Tick": str(timestamp),
                "V": item["v"]
            })
        return return_data
    except:
        return None


def get_all_futures():
    with open(os.path.join(os.path.dirname(__file__),"futures.json"), "r", encoding="utf-8") as file:
        futures = json.load(file)
        return futures


if __name__ == "__main__":
    print(get_kline_by_minutes("TA0", "60"))
