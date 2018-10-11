#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: function_custom.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/10 18:10
# @desc: 排序函数练习


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


# 根据姓名排序
sorted(L, key=by_name)

L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


# 根据分数排序
sorted(L, key=by_score)

L2 = sorted(L, key=by_score)
print(L2)
