#!/usr/bin/env python
# encoding: utf-8

import time
import sys
import datetime
import tushare as ts
from databases import models
from databases.db import Db
from utils import helper
from sqlalchemy import and_

db = Db()

def updateKiData():
    '''
    更新股票
    '''
    session = db.getDbsession()
    allStocks = session.query(models.Stocks.code).all()
    insertData = []
    timestamp = int(time.time())
    curDate = time.strftime("%Y-%m-%d", time.localtime(timestamp))
    for item in allStocks:
        code = item[0]
        query = session.query(models.StockKiData.code).filter(and_(models.StockKiData.code == code, models.StockKiData.date == curDate))

        isRealtime = True
        try:
            #大盘结束则取完整历史数据
            if datetime.datetime.now().hour > 15:
                df = ts.get_hist_data(code, curDate)
                isRealtime = False
            else:
                # 获取实时数据,数据不完整
                df = ts.get_realtime_quotes(code)
        except Exception, e:
            helper.log('updateKiData stock:{:^8}fail'.format(code))
            continue

        if query.first():
            if not isRealtime:
                query.update({
                    models.StockKiData.openPrice: df['open'][curDate],
                    models.StockKiData.highPrice: df['high'][curDate],
                    models.StockKiData.closePrice: df['close'][curDate],
                    models.StockKiData.lowPrice: df['low'][curDate],
                    models.StockKiData.volume: df['volume'][curDate],
                    models.StockKiData.priceChange:df['price_change'][curDate],
                    models.StockKiData.pChange: df['p_change'][curDate],
                    models.StockKiData.maFive: df['ma5'][curDate],
                    models.StockKiData.maTen: df['ma10'][curDate],
                    models.StockKiData.maTwenty: df['ma20'][curDate],
                    models.StockKiData.vMaFive: df['v_ma5'][curDate],
                    models.StockKiData.vMaTen: df['v_ma10'][curDate],
                    models.StockKiData.vMaTwenty: df['v_ma20'][curDate],
                    models.StockKiData.turnover: df['turnover'][curDate]
                })
            else:
                query.update({
                    models.StockKiData.openPrice: df['open'][0],
                    models.StockKiData.highPrice: df['high'][0],
                    models.StockKiData.closePrice: df['price'][0],
                    models.StockKiData.lowPrice: df['low'][0],
                    models.StockKiData.volume: df['volume'][0],
                })
            session.commit()
        else:
            insertData.append(models.StockKiData(
                code = code,
                openPrice = df['open'][0],
                highPrice = df['high'][0],
                closePrice = df['price'][0],
                lowPrice = df['low'][0],
                volume = df['volume'][0],
                date = df['date'][0],
                timestamp = int(time.mktime(time.strptime(df['date'][0], '%Y-%m-%d')))
            ))
            if len(insertData) >= 100:
                db.addData(insertData)
                insertData = []
    if insertData:
        db.addData(insertData)

def initKiData():
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
    df = ts.get_stock_basics()
    session = db.getDbsession()
    if df.empty:
        return False
    insertData = []
    for code in df.index:
        # 如果不是初始化数据则查询是否有该数据
        df = ts.get_hist_data(code)
        if df.empty:
            helper.log('lost ' + code)
            continue
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
        if len(insertData) >= 100:
            db.addData(insertData)
            insertData = []
    if insertData:
        db.addData(insertData)


def get_all_stock():
    """
    获取所有股票数据
        code,代码
        name,名称
        industry,所属行业
        area,地区
        pe,市盈率
        outstanding,流通股本(亿)
        totals,总股本(亿)
        totalAssets,总资产(万)
        liquidAssets,流动资产
        fixedAssets,固定资产
        reserved,公积金
        reservedPerShare,每股公积金
        esp,每股收益
        bvps,每股净资
        pb,市净率
        timeToMarket,上市日期
        undp,未分利润
        perundp, 每股未分配
        rev,收入同比(%)
        profit,利润同比(%)
        gpr,毛利率(%)
        npr,净利润率(%)
        holders,股东人数
    """
    df = ts.get_stock_basics()
    if df.empty:
        return False
    insertData = []
    session = db.getDbsession()
    for code in df.index:
        query = session.query(models.Stocks.name).filter(models.Stocks.code == code)
        # 如果存在则更新
        if query.first():
            query.update({
                models.Stocks.pe: df['pe'][code],
                models.Stocks.outstanding: df['outstanding'][code],
                models.Stocks.totals: df['totals'][code],
                models.Stocks.totalAssets: df['totalAssets'][code],
                models.Stocks.liquidAssets: df['liquidAssets'][code],
                models.Stocks.fixedAssets: df['fixedAssets'][code],
                models.Stocks.reserved: df['reserved'][code],
                models.Stocks.reservedPerShare: df['reservedPerShare'][code],
                models.Stocks.esp: df['esp'][code],
                models.Stocks.bvps: df['bvps'][code],
                models.Stocks.pb: df['pb'][code],
                models.Stocks.timeToMarket: df['timeToMarket'][code],
                models.Stocks.undp: df['undp'][code],
                models.Stocks.perundp: df['perundp'][code],
                models.Stocks.rev: df['rev'][code],
                models.Stocks.profit: df['profit'][code],
                models.Stocks.gpr: df['gpr'][code],
                models.Stocks.npr: df['npr'][code],
                models.Stocks.holders: df['holders'][code],
            })
            session.commit()
            continue
        insertData.append(models.Stocks(
            code = code,
            name = df['name'][code],
            industry = df['industry'][code],
            area = df['area'][code],
            pe = df['pe'][code],
            outstanding = df['outstanding'][code],
            totals = df['totals'][code],
            totalAssets = df['totalAssets'][code],
            liquidAssets = df['liquidAssets'][code],
            fixedAssets = df['fixedAssets'][code],
            reserved = df['reserved'][code],
            reservedPerShare = df['reservedPerShare'][code],
            esp = df['esp'][code],
            bvps = df['bvps'][code],
            pb = df['pb'][code],
            timeToMarket = df['timeToMarket'][code],
            undp = df['undp'][code],
            perundp = df['perundp'][code],
            rev = df['rev'][code],
            profit = df['profit'][code],
            gpr = df['gpr'][code],
            npr = df['npr'][code],
            holders = df['holders'][code],
        ))
        if len(insertData) >= 100:
            db.addData(insertData)
            insertData = []
    if insertData:
        db.addData(insertData)
    return True

def get_index():
    """
    获取大盘实时行情

    code:指数代码
    name:指数名称
    change:涨跌幅
    open:开盘点位
    preclose:昨日收盘点位
    close:收盘点位
    high:最高点位
    low:最低点位
    volume:成交量(手)
    amount:成交金额（亿元）
    """
    try:
        df = ts.get_index()
        insertData = []
        timestamp = int(time.time())
        date = time.strftime("%Y-%m-%d", time.localtime(timestamp))

        for index in df.index:
            insertData.append(models.Index(
                code = df['code'][index],
                name = df['name'][index],
                change = df['change'][index],
                open = df['open'][index],
                preclose = df['preclose'][index],
                close = df['close'][index],
                high = df['high'][index],
                low = df['low'][index],
                volume = df['volume'][index],
                amount = df['amount'][index],
                date = date,
                timestamp = timestamp
            ))
        if insertData:
            db.addData(insertData)
    except Exception, e:
        helper.log(e)

def calcUpOrDownPercent(beforeDay = 3):
    session = db.getDbsession()
    allStocks = session.query(models.StockKiData.code, models.StockKiData.close).filter()

if __name__ == '__main__':
    updateKiData()
