#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: function_custom.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/10 18:10
# @desc: 递归函数：汉诺塔练习


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        # move(1, a, b, c)
        print('move', a, '-->', c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
