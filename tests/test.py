def get_names():
    import requests

    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQFuturesData'

    headers = {
      "Accept": "*/*",
      "Accept-Language": "zh-CN,zh;q=0.9",
      "Connection": "keep-alive",
      "Content-type": "application/x-www-form-urlencoded",
      "Referer": "http://vip.stock.finance.sina.com.cn/quotes_service/view/qihuohangqing.html",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    cookies={
      "SINAGLOBAL": "137.175.84.92_1726105611.419815",
      "Apache": "137.175.84.92_1726105611.419815",
      "UOR": "vip.stock.finance.sina.com.cn,finance.sina.com.cn,",
      "ULV": "1726105725925:1:1:1:137.175.84.92_1726105611.419815:",
      "SFA_version7.25.0": "2024-09-12%2009%3A45",
      "SFA_version7.25.0_click": "1",
      "FIN_ALL_VISITED": "TA2501%2CV0",
      "NEWESTVISITED_FUTURE": "%7B%22code%22%3A%22TA2501%22%2C%22hqcode%22%3A%22nf_TA2501%22%2C%22type%22%3A1%7D%7C%7B%22code%22%3A%22V0%22%2C%22hqcode%22%3A%22nf_V0%22%2C%22type%22%3A1%7D"
    }

    params={
      "page": "1",
      "sort": "position",
      "asc": "0",
      "node": "pta_qh",
      "base": "futures"
    }


    # 发送GET请求
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    unclean_data = response
    return_data = []
    for i in unclean_data:
        return_data.append(i['name'])

