#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Column, VARCHAR, Integer, Float, DATE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base();

class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', VARCHAR(255))
    password = Column('password', VARCHAR(64))

class StockKiData(Base):
    "日Ｋ线数据"
    __tablename__ = 'stock_k_data'

    id = Column('id', Integer, primary_key=True)
    # 股票代码
    code        = Column('code', VARCHAR(10), server_default = "")
    # 开盘价格
    openPrice   = Column('open_price', Float, server_default = "0")
    # 最高价格
    highPrice   = Column('high_price', Float, server_default = "0")
    # 收盘价格
    closePrice  = Column('close_price', Float, server_default = "0")
    # 最低价格
    lowPrice    = Column('low_price', Float, server_default = "0")
    # 成交量
    volume      = Column('volume', Float, server_default = "0")
    # 价格变化量
    priceChange = Column('price_change', Float, server_default = "0")
    # 涨跌幅度
    pChange     = Column('p_change', Float, server_default = "0")
    # 5日均价
    maFive      = Column('ma_five', Float, server_default = "0")
    # 10日均价
    maTen       = Column('ma_ten', Float, server_default = "0")
    # 20日均价
    maTwenty    = Column('ma_twenty', Float, server_default = "0")
    # 5日均量
    vMaFive     = Column('v_ma_five', Float, server_default = "0")
    # 10日均量
    vMaTen      = Column('v_ma_ten', Float, server_default = "0")
    # 20日均量
    vMaTwenty   = Column('v_ma_twenty', Float, server_default = "0")
    # 换手率
    turnover    = Column('turnover', Float, server_default = "0")
    # 日期
    date        = Column('k_date', DATE)
    # unix日期
    timestamp   = Column('timestamp', Integer, server_default = "0")

class Stocks(Base):
    "股票列表"
    __tablename__ = 'stocks'

    id = Column('id', Integer, primary_key=True)
    code = Column('code', VARCHAR(10), server_default = "") # 股票代码
    name = Column('name', VARCHAR(64), server_default = "") # 股票名称
    industry = Column('industry', VARCHAR(255), server_default = "") # 所属行业
    area = Column('area', VARCHAR(255), server_default = "") # 地区
    pe = Column('pe', Float, server_default = "0") # 市盈率
    outstanding = Column('outstanding', Float, server_default = "0") # 流通股本(亿)
    totals = Column('totals', Float, server_default = "0") # 总股本(亿)
    totalAssets = Column('total_assets', Float, server_default = "0") # 总资产(万)
    liquidAssets = Column('liquid_assets', Float, server_default = "0") # 流动资产
    fixedAssets = Column('fixed_assets', Float, server_default = "0") # 固定资产
    reserved = Column('reserved', Float, server_default = "0") # 公积金
    reservedPerShare = Column('reserved_per_share', Float, server_default = "0") # 每股公积金
    esp = Column('esp', Float, server_default = "0") # 每股收益
    bvps = Column('bvps', Float, server_default = "0") # 每股净资
    pb = Column('pb', Float, server_default = "0") # 市净率
    timeToMarket = Column('time_to_market', Float, server_default = "0") # 上市日期
    undp = Column('undp', Float, server_default = "0") # 未分利润
    perundp = Column('perundp', Float, server_default = "0") # 每股未分配
    rev = Column('rev', Float, server_default = "0") # 收入同比(%)
    profit = Column('profit', Float, server_default = "0") # 利润同比(%)
    gpr = Column('gpr', Float, server_default = "0") # 毛利率(%)
    npr = Column('npr', Float, server_default = "0") # 净利润率(%)
    holders = Column('holders', Float, server_default = "0") # 股东人数

class StockPe(Base):
    "股票市盈率"
    __tablename__ = 'stock_pe'

    id = Column('id', Integer, primary_key=True)
    code = Column('code', VARCHAR(10), server_default = "") # 股票代码
    name = Column('name', VARCHAR(64), server_default = "") # 股票名称
    industry = Column('industry', VARCHAR(255), server_default = "") # 所属行业
    area = Column('area', VARCHAR(255), server_default = "") # 地区
    pe = Column('pe', Float, server_default = "0") # 市盈率
    outstanding = Column('outstanding', Float, server_default = "0") # 流通股本(亿)
    totals = Column('totals', Float, server_default = "0") # 总股本(亿)
    totalAssets = Column('total_assets', Float, server_default = "0") # 总资产(万)
    liquidAssets = Column('liquid_assets', Float, server_default = "0") # 流动资产
    fixedAssets = Column('fixed_assets', Float, server_default = "0") # 固定资产
    reserved = Column('reserved', Float, server_default = "0") # 公积金
    reservedPerShare = Column('reserved_per_share', Float, server_default = "0") # 每股公积金
    esp = Column('esp', Float, server_default = "0") # 每股收益
    bvps = Column('bvps', Float, server_default = "0") # 每股净资
    pb = Column('pb', Float, server_default = "0") # 市净率
    timeToMarket = Column('time_to_market', Float, server_default = "0") # 上市日期
    undp = Column('undp', Float, server_default = "0") # 未分利润
    perundp = Column('perundp', Float, server_default = "0") # 每股未分配
    rev = Column('rev', Float, server_default = "0") # 收入同比(%)
    profit = Column('profit', Float, server_default = "0") # 利润同比(%)
    gpr = Column('gpr', Float, server_default = "0") # 毛利率(%)
    npr = Column('npr', Float, server_default = "0") # 净利润率(%)
    holders = Column('holders', Float, server_default = "0") # 股东人数
