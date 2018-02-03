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

def get_transaction_record(code, date=None, period=3):
    """
        获取此股近期交易记录
            code stock number
            date the begin date, default is last trade date
            period the length of the record
    Return
    --------
    DataFrame
               price,价格
               volume,数量
               amount,金额
               current_profit,当前的期望获利值
    """
    #stock_basic_info = get_stock_basics(code)
    last_trade_date = tddate.last_tddate(date)
    trade_data = []
    for i in range(period):
        temp_tddate = tddate.delta_tddate(last_trade_date,-i)
        temp_data = ts.get_tick_data(code, temp_tddate)
        temp_data = temp_data.drop(['change'],axis=1)
        for i in range(temp_data.shape[0]):
            temp_data.loc[i,'time'] = temp_tddate + ' ' + temp_data['time'][i]
        trade_data.append(temp_data)
    trade_data = pd.concat(trade_data)
    trade_data.index = range(trade_data.shape[0])
    return trade_data
    
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
    print(get_transaction_record('600848',period=5))
    