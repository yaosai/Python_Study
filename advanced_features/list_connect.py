#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: function_custom.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/9/12 10:03
# @desc: 列表生成式


import os

L = list(range(1, 11))
print(L)

L = [x * x for x in range(1, 11)]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = [m + n for m in 'ABC' for n in 'DEF']
print(L)

path = "C:/Users/yaosai/Desktop/"
L = [d for d in os.listdir(path)]
print(L)

m = {'x': '111', 'y': '222', 'z': '333'}
for k, v in m.items():
    print(k, '=', v)

# 相当于列表循环嵌套
L = [k + '=' + v for k, v in m.items()]
print(L)

n = {'x': 111, 'y': 222, 'z': 333}
L = [k + '=' + str(v) for k, v in n.items()]
print(L)
