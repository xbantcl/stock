#!/usr/bin/env python
# encoding: utf-8

import tushare as ts


def get_k_data(code):
    """
        获取k线图值
    """
    df = ts.get_k_data(code)

