from Ashare import *
    
# 证券代码兼容多种格式 通达信，同花顺，聚宽
# sh000001 (000001.XSHG)    sz399006 (399006.XSHE)   sh600519 ( 600519.XSHG )
df = get_price('P0805.XSHG',frequency='5m',count=100)
# records = df.to_dict(orient='records')
#
# # 重置索引为列
# records_with_dates = [{'date': idx.strftime('%Y-%m-%d %H:%M:%S'), **record} for idx, record in zip(df.index, records)]
#
# # 查看结果
# print(records_with_dates)
print(df)
