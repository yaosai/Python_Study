#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: other.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/10 23:09
# @desc: 特殊方法

# 查看函数文档
help(print)
print(print.__doc__)


# 定义文档
def func():
    """
    这是文档
    """
    pass


help(func)
print(func.__doc__)
