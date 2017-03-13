#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Table, Column, VARCHAR, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base();


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', VARCHAR(255))
    password = Column('password', VARCHAR(64))

class StockKiData(Base):
    __tablename__ = 'stock_k_data'
    # 开盘价格
    openPrice   = Column('open_price', Float)
    # 最高价格
    highPrice   = Column('high_price', Float)
    # 收盘价格
    closePrice  = Column('close_price', Float)
    # 最低价格
    lowPrice    = Column('low_price', Float)
    # 成交量
    volume      = Column(Float)
    # 价格变化量
    priceChange = Column('price_change', Float)
    # 涨跌幅度
    pChange     = Column('p_change', Float)
    # 5日均价
    maFive      = Column('ma_five', Float)
    # 10日均价
    maTen       = Column('ma_ten', Float)
    # 20日均价
    maTwenty    = Column('ma_twenty', Float)
    # 5日均量
    vMaFive     = Column('v_ma_five', Float)
    # 10日均量
    vMaTen      = Column('v_ma_ten', Float)
    # 20日均量
    vMaTwenty   = Column('v_ma_twenty', Float)
    # 换手率
    turnover    = Column('turnover', Float)
