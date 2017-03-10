#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker

mysqlDsn = 'mysql+mysqldb://admin:O!g3L70B%F@172.17.0.5/monitor'
engine = create_engine(mysqlDsn, echo=True)
Base = declarative_base()
# 获取元数据
metadata = MetaData()



