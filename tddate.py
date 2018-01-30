# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:06:34 2018

@author: HEZH
"""
import datetime
from tushare.util import dateu as du

# 开市日历
du = du.trade_cal()
du = du[(du['isOpen']==1) & (du['calendarDate']>'2010-01-01')]
OPEN_CAL = du.to_dict('list')['calendarDate']

def last_tddate(date=None):
    """
        获取最近一个交易日
    """
    if date==None:
        today = datetime.datetime.now()
        if today.strftime('%H') < '18':
            today = today - datetime.timedelta(days=1)
        date = today.strftime("%Y-%m-%d")
    for td_date in OPEN_CAL[::-1]:
        if td_date<=date:
            return td_date
    return None

def delta_date(date, delta):
    """
        获取相对日期
        参数：
            date 为参考日期例如 '2018-01-29'
            delta 为相对间隔日期
        return
            相对间隔天数的日期
    """
    temp_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    result_date = temp_date + datetime.timedelta(days=delta)
    return result_date.strftime("%Y-%m-%d")

def delta_tddate(date, delta):
    """
        获取相对交易日
        参数：
            date 为参考日期例如 '2018-01-29'
            delta 为相对间隔日期
        return
            相对间隔日期的交易日
    """
    date = last_tddate(date)
    date_index = OPEN_CAL.index(date)
    return OPEN_CAL[date_index+delta]

if __name__ == '__main__':
    print(last_tddate('2018-01-28'))
    print(delta_date('2018-01-27',7))
    print(delta_tddate('2018-01-27',7))
  