# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:06:29 2018

@author: Genius
"""

import tushare as ts
from tushare.util import dateu as du
import datetime

#print(ts.get_hist_data('600848'))
#print(ts.get_stock_basics())
#for a in ts.get_stock_basics().axes[0]:
#    print(a)
#print(list(ts.get_stock_basics().axes[0]))
#print(ts.get_today_all())
df = ts.get_tick_data('600848',date='2018-01-30')
df = df + ts.get_tick_data('600848',date='2018-01-29')
#df = ts.get_realtime_quotes('000581')
#df = ts.get_today_ticks('601333')
#df = ts.get_stock_basics()
#du = du.trade_cal()
#du = du[(du['isOpen']==1) & (du['calendarDate']>'2010-01-01')]
#du = du.to_dict('list')['calendarDate']
#du.reverse()
#print(du)
print(df)
#print(df.to_dict('index')['300104'])
#today = datetime.datetime.now()
#print(today.strftime('%H'))
#print(datetime.datetime.strptime('2017-01-01', "%Y-%m-%d"))
#temp_date = datetime.datetime.strptime('2010-01-01', "%Y-%m-%d")
#result_date = temp_date + datetime.timedelta(days=-1)
#print(result_date.strftime("%Y-%m-%d"))