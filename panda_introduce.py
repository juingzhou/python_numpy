#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 21:52
# @Author : juingzhou
# @Site : 
# @File : panda_introduce.py
# @Software: PyCharm
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
dates = pd.date_range('20180604', periods=7)
print(dates)
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
