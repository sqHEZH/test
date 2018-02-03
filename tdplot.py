#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:56:15 2018

@author: hezhu
"""

import tdlib

def tdprice_distribution(code, date=None, period=3):
    """
        获取最近一个交易日
    """
    td_records = tdlib.get_transaction_record(code, date, period)
    if date==None:
        today = datetime.datetime.now()
        if today.strftime('%H') < '18':
            today = today - datetime.timedelta(days=1)
        date = today.strftime("%Y-%m-%d")
    for td_date in OPEN_CAL[::-1]:
        if td_date<=date:
            return td_date
    return None

if __name__ == '__main__':
    print()