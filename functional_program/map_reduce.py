#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: function_custom.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/10 18:10
# @desc: MapReduce函数练习
from functools import reduce

l1 = [i for i in range(1, 10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)

print(l2)


def mp(n):
    return n * 10


# 利用map函数实现同样的功能
l3 = map(mp, l1)
print(type(l3))
for i in l3:
    print(i)


def add(x, y):
    return x + y


print(reduce(add, l1))
