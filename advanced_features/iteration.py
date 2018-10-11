#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# from collections import Iterable

# @file: function_custom.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/9/11 10:21
# @desc: 迭代demo


# d = {1: 'a', 2: 'b', 3: 'c'}
# for k in d:
#     print(k)
# for v in d.values():
#     print(v)
# for v in 'abcde':
#     print(v)
#
# isinstance('abcde', Iterable)

# L = [12, 34, 11, 3, 56]


# 利用迭代求数组最大最小值
def find_min_and_max(l):
    if len(l) == 0:
        return None, None
    else:
        max = l[0]
        min = l[0]
        for m in l:
            if m > max:
                max = m
            if m < min:
                min = m
        return min, max


# 方法优化
# def find_min_and_max(L):
#     if L == []:
#         return (None, None)
#     else:
#         return (min(L), max(L))


# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
