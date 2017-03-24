#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Column, VARCHAR, Integer, Float, create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base

mysqlDsn = 'mysql+mysqldb://admin:O!g3L70B%F@172.17.0.4/stock'
engine = create_engine(mysqlDsn, echo=True)

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


def initDb():
    Base.metadata.create_all(engine)

def dropDb():
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    dropDb()
    initDb()
