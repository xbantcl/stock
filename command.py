#!/usr/bin/env python
# encoding: utf-8

import types
import time
import tushare as ts
from databases import models
from databases.db import Db

def get_k_data(code):
    """
    获取历史k线图值
        date：日期
        open：开盘价
        high：最高价
        close：收盘价
        low：最低价
        volume：成交量
        price_change：价格变动
        p_change：涨跌幅
        ma5：5日均价
        ma10：10日均价
        ma20:20日均价
        v_ma5:5日均量
        v_ma10:10日均量
        v_ma20:20日均量
        turnover:换手率[注：指数无此项]
    """
    df = ts.get_hist_data(code)
    insertData = []
    for index in df.index:
        insertData.append(models.StockKiData(
            code = code,
            openPrice = df['open'][index],
            highPrice = df['high'][index],
            closePrice = df['close'][index],
            lowPrice = df['low'][index],
            volume = df['volume'][index],
            priceChange = df['price_change'][index],
            pChange = df['p_change'][index],
            maFive = df['ma5'][index],
            maTen = df['ma10'][index],
            maTwenty = df['ma20'][index],
            vMaFive = df['v_ma5'][index],
            vMaTen = df['v_ma10'][index],
            vMaTwenty = df['v_ma20'][index],
            turnover = df['turnover'][index],
            date = index,
            timestamp = int(time.mktime(time.strptime(index, "%Y-%m-%d")))
        ))
    if insertData:
        addData(insertData)

def addData(insertData):
    "添加数据"
    db = Db()
    session = db.getDbsession()
    if types.ListType == type(insertData):
        session.add_all(insertData)
    else:
        session.add(insertData)
    session.commit()


if __name__ == '__main__':
    get_k_data('000838')
