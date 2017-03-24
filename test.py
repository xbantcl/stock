#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# 获取元数据
metadata = MetaData()



