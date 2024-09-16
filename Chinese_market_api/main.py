from flask import Flask, jsonify
from flask_caching import Cache
from flask_cors import CORS

from outer_api.a_stock.All_bonds_and_prices import bonds_and_prices
from outer_api.a_stock.Ashare import *
from outer_api.future.future_tools import *


app = Flask(__name__)
CORS(app)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

'''
A股/国债接口
'''

@app.route('/stock/kline_5m/<bond_code>', methods=['GET'])
@cache.cached(timeout=2)
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
        return_data = []
        for record in records_with_dates:
            return_data.append({
                "C": str(record['close']),
                "H": str(record['high']),
                "L": str(record['low']),
                "O": str(record['open']),
                "V": str(record['volume']),
                "Tick": str(record['date'])
            })
        return jsonify(return_data)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('/stock/kline_1m/<bond_code>', methods=['GET'])
@cache.cached(timeout=2)
def kline_1m(bond_code):
    if not bond_code:
        return {
            'error': '需传递bond_code参数，例:sh000001'
        }
    try:
        df = get_price(code=bond_code, frequency="1m", count=200)
        records = df.to_dict(orient='records')
        print(records)
        # 重置索引为列
        records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
        return_data = []
        for record in records_with_dates:
            return_data.append({
                "C": str(record['close']),
                "H": str(record['high']),
                "L": str(record['low']),
                "O": str(record['open']),
                "V": str(record['volume']),
                "Tick": str(record['date'])
            })
        return jsonify(records_with_dates)
    except Exception as e:
        return jsonify([])


@app.route('/stock/kline_15m/<bond_code>', methods=['GET'])
@cache.cached(timeout=2)
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
        return_data = []
        for record in records_with_dates:
            return_data.append({
                "C": str(record['close']),
                "H": str(record['high']),
                "L": str(record['low']),
                "O": str(record['open']),
                "V": str(record['volume']),
                "Tick": str(record['date'])
            })
        return jsonify(return_data)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('/stock/kline_30m/<bond_code>', methods=['GET'])
@cache.cached(timeout=2)
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
        return_data = []
        for record in records_with_dates:
            return_data.append({
                "C": str(record['close']),
                "H": str(record['high']),
                "L": str(record['low']),
                "O": str(record['open']),
                "V": str(record['volume']),
                "Tick": str(record['date'])
            })
        return jsonify(return_data)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('/stock/kline_60m/<bond_code>', methods=['GET'])
@cache.cached(timeout=2)
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
        return_data = []
        for record in records_with_dates:
            return_data.append({
                "C": str(record['close']),
                "H": str(record['high']),
                "L": str(record['low']),
                "O": str(record['open']),
                "V": str(record['volume']),
                "Tick": str(record['date'])
            })
        return jsonify(return_data)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('/stock/kline_1d/<bond_code>', methods=['GET'])
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
        return_data = []
        for record in records_with_dates:
            return_data.append({
                "C": str(record['close']),
                "H": str(record['high']),
                "L": str(record['low']),
                "O": str(record['open']),
                "V": str(record['volume']),
                "Tick": str(record['date'])
            })
        return jsonify(return_data)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('/stock/kline_1w/<bond_code>', methods=['GET'])
@cache.cached(timeout=6000 * 3)
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
        return_data = []
        for record in records_with_dates:
            return_data.append({
                "C": str(record['close']),
                "H": str(record['high']),
                "L": str(record['low']),
                "O": str(record['open']),
                "V": str(record['volume']),
                "Tick": str(record['date'])
            })
        return jsonify(return_data)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('/stock/kline_1M/<bond_code>', methods=['GET'])
@cache.cached(timeout=6000 * 3)
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
        return_data = []
        for record in records_with_dates:
            return_data.append({
                "C": str(record['close']),
                "H": str(record['high']),
                "L": str(record['low']),
                "O": str(record['open']),
                "V": str(record['volume']),
                "Tick": str(record['date'])
            })
        return jsonify(return_data)
    except Exception as e:
        app.logger.error(f"Error fetching kline data for {bond_code}: {e}")
        return f"Error fetching kline data for {bond_code}: {e}"


@app.route('/stock/bonds_and_prices', methods=['GET'])
@cache.cached(timeout=8)
def get_bonds_and_prices():
    return jsonify(bonds_and_prices())


'''
期货接口
'''
@app.route('/future/futures', methods=['GET'])
@cache.cached(timeout=60)
def _get_all_futures():
    return jsonify(get_all_futures())

@app.route('/future/kline_1m/<future_code>', methods=['GET'])
@cache.cached(timeout=2)
def future_kline_1m(future_code):
    return jsonify(get_kline_by_minutes(future_code, "1"))

@app.route('/future/kline_5m/<future_code>', methods=['GET'])
@cache.cached(timeout=2)
def future_kline_5m(future_code):
    return jsonify(get_kline_by_minutes(future_code, "5"))

@app.route('/future/kline_10m/<future_code>', methods=['GET'])
@cache.cached(timeout=2)
def future_kline_10m(future_code):
    return jsonify(get_kline_by_minutes(future_code, "10"))

@app.route('/future/kline_15m/<future_code>', methods=['GET'])
@cache.cached(timeout=2)
def future_kline_15m(future_code):
    return jsonify(get_kline_by_minutes(future_code, "15"))

@app.route('/future/kline_30m/<future_code>', methods=['GET'])
@cache.cached(timeout=2)
def future_kline_30m(future_code):
    return jsonify(get_kline_by_minutes(future_code, "30"))


@app.route('/future/kline_60m/<future_code>', methods=['GET'])
@cache.cached(timeout=2)
def future_kline_60m(future_code):
    return jsonify(get_kline_by_minutes(future_code, "60"))





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5626, debug=False)
