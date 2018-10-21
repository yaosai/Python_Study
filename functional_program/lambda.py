#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: lambda.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/20 23:29
# @desc: lambda表达式

# lambda表达式是匿名函数
# 以lambda开头，紧跟参数，逗号隔开，冒号后跟函数主体

stm1 = lambda x: x * 100
print(stm1(10))

stm2 = lambda x, y: x * y
print(stm2(10, 10))


# 定义函数A
def funA(n):
    return n * 10


# 定义函数B
def funB(n):
    return n * 3


def funC(n, f):
    return f(n) * 3


# 将函数B传入函数A
print(funA(funB(5)))
print(funC(5, funA))
