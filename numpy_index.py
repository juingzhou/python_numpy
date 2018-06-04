#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 20:46
# @Author : juingzhou
# @Site : 
# @File : numpy_index.py
# @Software: PyCharm

import numpy as np

a = np.arange(3, 15).reshape(3, 4)  # 三行四列
print(a)
print(a[:1, 2])
print(a.flatten())  # 迭代器
for column in a.T:  # 迭代a的列
    print(column)
for row in a.flat:
    print(row, end=' ')
