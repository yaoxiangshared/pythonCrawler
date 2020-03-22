# coding=utf-8

import tushare as ts
import time
from collections import Iterable
from functools import reduce


def m30(code):
    startDate = time.strftime("%Y-%m-%d", time.localtime(time.time() - 24 * 3600 * 30))
    endDate = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # print(startDate)
    # print(endDate) 
    df = ts.get_hist_data(code, startDate, endDate)

    closeList = df['close'].to_list()

    def add(x, y):
        return x + y

    sum = reduce(add, closeList)
    return round(sum / len(closeList), 2)


stockList = ts.get_zz500s()
startDate = time.strftime("%Y-%m-%d", time.localtime(time.time() - 24 * 3600 * 5))
endDate = time.strftime("%Y-%m-%d", time.localtime(time.time()))
goodStock1 = goodStock2 = {};
for index, row in stockList.iterrows():
    code = row["code"]
    name = row["name"]
    print(name)
    print(code)
    m30 = m30(code)
    print(m30)
    df = ts.get_hist_data(code, startDate, endDate)
    closeList = df['close'].to_list()
    result = list(filter(lambda x: x > m30, closeList))
    if len(result) == len(closeList):
        goodStock1[code] = name
    todayClose = closeList[-1]
    if todayClose >= m30 and todayClose <= 1.05 * m30:
        goodStock2[code] = name

    time.sleep(2)
    # break

print('最近5天收盘价格都大于30日均价:')
print(goodStock1)
print('30日均价 <= 今日收盘价格 <= 30日均价*1.05:')
print(goodStock2)
