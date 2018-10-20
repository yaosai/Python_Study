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
