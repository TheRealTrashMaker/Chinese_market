from flask import Flask, jsonify, request
from flask_caching import Cache
from flask_cors import CORS
from Chinese_market_api.outer_api.a_stock.All_bonds_and_prices import bonds_and_prices
from Chinese_market_api.outer_api.a_stock.Ashare import *

app = Flask(__name__)
CORS(app)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route('stock/kline_5m/<bond_code>', methods=['GET'])
@cache.cached(timeout=60)
def kline_5m(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="5m", count=100)
        records = df.to_dict(orient='records')

        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return jsonify(records_with_dates)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('stock/kline_1m/<bond_code>', methods=['GET'])
@cache.cached(timeout=2)
def kline_1m(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="1m", count=200)
        records = df.to_dict(orient='records')

        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return jsonify(records_with_dates)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('stock/kline_15m/<bond_code>', methods=['GET'])
@cache.cached(timeout=300)
def kline_15m(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="15m", count=200)
        records = df.to_dict(orient='records')

        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return jsonify(records_with_dates)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('stock/kline_30m/<bond_code>', methods=['GET'])
@cache.cached(timeout=600)
def kline_30m(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="30m", count=200)
        records = df.to_dict(orient='records')

        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return jsonify(records_with_dates)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('stock/kline_60m/<bond_code>', methods=['GET'])
@cache.cached(timeout=1800)
def kline_60m(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="60m", count=100)
        records = df.to_dict(orient='records')

        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return jsonify(records_with_dates)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('stock/kline_1d/<bond_code>', methods=['GET'])
@cache.cached(timeout=6000)
def kline_1d(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="1d", count=200)
        records = df.to_dict(orient='records')

        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return jsonify(records_with_dates)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('stock/kline_1w/<bond_code>', methods=['GET'])
@cache.cached(timeout=6000*3)
def kline_1w(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="1w", count=200)
        records = df.to_dict(orient='records')

        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return jsonify(records_with_dates)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('stock/kline_1M/<bond_code>', methods=['GET'])
@cache.cached(timeout=6000*3)
def kline_1M(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="1M", count=200)
        records = df.to_dict(orient='records')

        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return jsonify(records_with_dates)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('stock/bonds_and_prices', methods=['GET'])
@cache.cached(timeout=8)
def get_bonds_and_prices():
    return jsonify(bonds_and_prices())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5608, debug=False)
