#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/31 19:46
# @Author : juingzhou
# @Site : 
# @File : numpy基本运算.py
# @Software: PyCharm
# 基本运算
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.arange(5)
c = a - b
print(c)
print(c * 2)
print(b ** 2)
print(a * np.sin(30))
print(a < 35)  # 判断a数组里面哪些数小于35
a *= 2  # 更改已存在数组a
print(a)
d = np.arange(1, 5).reshape(2, 2)#两行两列
e = np.arange(4).reshape(2, 2)#两行两列
print(np.dot(d, e))  # 矩阵乘法

f = np.random.random((2, 3))
print(f)
print(f.sum())
print(f.sum(axis=0))  # sum of each column
print(f.sum(axis=1))  # sum of each row
print(f.min())
print(f.min(axis=0))  # min of each column
print(f.min(axis=1))  # min of each row
print(f.max())
print(f.max(axis=0))
print(f.max(axis=1))
print(f.cumsum(axis=1))  # cumulative sum along each row
print(f.cumsum(axis=0))  # cumulative sum along each column
g = np.arange(15).reshape(3,5)
print(np.exp(g*1j))
print(np.argmin(g))#最大数
print(np.argmax(g))#最大数
print(np.mean(g))#平均数
print(np.median(g))#中位数
print(np.cumsum(g ))#累加
print(np.nonzero(g))#输出非零数
print(g.T)#矩阵的转置
print(-np.sort(-g,axis=1))#降序


