#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 21:16
# @Author : juingzhou
# @Site : 
# @File : numpy_array分割.py
# @Software: PyCharm

import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
print(np.split(a, 2, axis=1))  # 纵向分割2块
print(np.split(a, 3, axis=0))  # 横向分割3块
print(np.array_split(a, 3, axis=1))  # 纵向分割3块
print(np.hsplit(a, 2))  # 纵向分割2块
print(np.vsplit(a, 3))  # 横向分割3块
