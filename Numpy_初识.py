#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/31 18:50
# @Author : juingzhou
# @Site : 
# @File : Numpy_初识.py
# @Software: PyCharm

import numpy as np

'''
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
1.object 任何暴露数组接口方法的对象都会返回一个数组或任何（嵌套）序列。
2.dtype 数组的所需数据类型，可选。
3.copy 可选，默认为true，对象是否被复制。
4.order C（按行）、F（按列）或A（任意，默认）。
5.subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
6.ndimin 指定返回数组的最小维数。
'''
# 一维数组
a = np.array([1, 2, 3],ndmin=2)#最小维度为2
print(a)

# 二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print("数组维度：%s"%b.ndim)#数组维度
print("数组形状：",b.shape)#数组形状，返回元祖(行数，列数)
print("数组元素：%s"%b.size)#数组元素

c = np.zeros([3,4])
print(c)

d =np.ones([3,4])
print(d)


e = np.arange(15).reshape(3,5)
print(e.ndim)

f = np.empty((2,3))#创建一个内容随机并且依赖与内存状态的数组
print(f)

g = np.arange(0,15)#返回数组不是列表
print(type(g))

h = np.linspace(0,10,20).reshape(2,10)#从零开始到10这个范围内生成20个随机数
print(h)