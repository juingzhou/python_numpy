#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 20:56
# @Author : juingzhou
# @Site : 
# @File : numpy_array合并.py
# @Software: PyCharm
import numpy as np

a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
print(np.vstack((a, b)))  # vetical stack数组合并
print(a.shape)  # 数组形状，返回元祖(行数，列数)
print(b.shape)  # 数组形状，返回元祖(行数，列数)
print(np.hstack((a, b)).shape)  # horizontal stack数组合并
print(np.hstack((a, b)))  # horizontal stack数组合并
print(a.reshape(3, 1))
print(a.reshape(1, 3))
print("vstack:",np.vstack((a.reshape(3, 1), b.reshape(3, 1))))
print("vstack:",np.vstack((a.reshape(1,3), b.reshape(1, 3))))
a = np.array([1, 1, 1]).reshape(3, 1)
b = np.array([2, 2, 2]).reshape(3, 1)
print(np.concatenate((a, b, b, a), axis=1))
