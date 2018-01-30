# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:03:03 2018

@author: HEZH
"""
import tushare as ts
import tddate
import pandas as pd

# 沪深所有股票
#ALL_STOCKS = ts.get_stock_basics().to_dict('index')

def get_price_distribution(code, date=None, period=3):
    """
        获取此股近期股票的价格分布
    Return
    --------
    DataFrame
               price,价格
               volume,数量
               amount,金额
               current_profit,当前的期望获利值
    """
    stock_basic_info = get_stock_basics(code)
    last_trade_date = tddate.last_tddate(date)
    trade_data = []
    for i in range(period):
        trade_data.append(ts.get_tick_data(code, tddate.delta_tddate(last_trade_date,-i)))
    trade_data = pd.concat(trade_data)
    return trade_data.reindex()
            
    
def get_expect_profit(code, date=None):
    """
        获取此股当天的期望收益
    Return 期望收益
    """
    pass

def get_expect_profit_distribution(code, date_begin=None, date_end=None):
    """
        获取此股期望收益的分布
    Return
    --------
    DataFrame
               h_price,持有价
               market_price,市场价
               profit,获利额
               change,变化
    """
    pass

if __name__ == '__main__':
    print(get_price_distribution('600848',period=3))
    