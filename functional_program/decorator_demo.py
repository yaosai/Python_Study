#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: decorator_demo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/21 13:49
# @desc: decorator装饰器和偏函数

import time
import functools


# 使用装饰器(Decorator)
# 调用函数打印当前时间
# 定义打印时间装饰器
def printTime(f):
    def wraaper(*args, **kwargs):
        print(time.ctime())
        return f(*args, **kwargs)

    return wraaper


# @+函数名，@是python的语法糖，使用@调用装饰器
@printTime
def hello():
    print("hello world")


f = hello
f()


# 手动执行装饰器

def hello2():
    print("hello world2")


# 将当前函数传入装饰器
hello2 = printTime(hello2)
hello2()

# 偏函数
# 参数固定的函数体
# 偏函数：functools.partial(int, base=16)：将int函数的base参数固定为16
int16 = functools.partial(int, base=16)
print(int16("12345"))
