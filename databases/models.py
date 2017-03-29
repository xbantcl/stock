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

# 日Ｋ线数据
class StockKiData(Base):
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

