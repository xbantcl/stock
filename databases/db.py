#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

from models import User

class Db(object):
    '''
    数据库类
    '''

    def __init__(self):
        "初始化数据库引擎"
        self.mysqlDsn = 'mysql+mysqldb://admin:O!g3L70B%F@172.17.0.5/stock'
        self.engine = self.getEngine()

    def initDb(self):
        "初始化数据库表结构"
        Base.metadata.create_all(self.engine)

    def dropDb(self):
        Base.metadata.drop_all(self.engine)

    def getEngine(self):
        return create_engine(self.mysqlDsn, echo=True)

    def getDbsession(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

if __name__ == '__main__':
    db = Db()
    db.dropDb()
    db.initDb()
