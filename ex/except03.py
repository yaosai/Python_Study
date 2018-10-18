#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: except01.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/19 1:46
# @desc: 自定义异常


# 定义一个error类，继承自系统error的子类
class MyError(ValueError):
    pass


try:
    print("手动产生异常raise")
    raise MyError
except ZeroDivisionError as e:
    print("输入错误！")
    exit()
except MyError as e:
    print("自定义的error")
except NameError as e:
    print("名称错误！")
    exit()
except ArithmeticError as e:
    print("属性错误！")
    exit()
finally:
    print("执行结束")
