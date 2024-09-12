import requests
from flask import Flask, jsonify
from flask_caching import Cache
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})


def bonds_and_prices():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }
    url = "https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeDataSimple"
    params = {
        "page": "1",
        "num": "20000",
        "sort": "symbol",
        "asc": "1",
        "node": "hs_z",
        "_s_r_a": "init"
    }
    try:
        response = requests.get(url, headers=headers, params=params).json()
        return response
    except:
        return None


@app.route('/bonds_and_prices', methods=['GET'])
@cache.cached(timeout=8)
def get_bonds_and_prices():
    return jsonify(bonds_and_prices())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5608, debug=False)
