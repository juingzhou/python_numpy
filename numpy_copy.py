#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 21:30
# @Author : juingzhou
# @Site : 
# @File : numpy_copy.py
# @Software: PyCharm

import numpy as np

a = np.arange(4)
print(a)
b = a
c = b
d = np.copy(a)
e = a.copy()
a[0] = 4
print(b)
print(c)
print(d is a)
print(e is a)

