#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: except01.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/19 1:46
# @desc: 手动捕获异常

# raise手动捕获异常，异常后语句不执行
try:
    print("手动产生异常raise")
    raise ArithmeticError
    print("产生异常后语句测试")
except ZeroDivisionError as e:
    print("输入错误！")
    print(type(e))
    print(e)
    exit()
except NameError as e:
    print("名称错误！")
    exit()
except ArithmeticError as e:
    print("属性错误！")
    exit()
finally:
    print("执行结束")
