#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: except01.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/19 1:46
# @desc: 异常处理


# 语法：
# try:
# <语句>        #运行可能抛出异常的代码
# except <名字>：
# <语句>        #如果在try部份引发了'name'异常
# except <名字>，<数据>:
# <语句>        #如果引发了'name'异常，获得附加的数据
# else:
# <语句>        #如果没有异常发生执行代码块
# finally:
# <语句>        #最后一定运行代码
try:
    num = int(input("请输入数字"))
    rst = 100 / num
    print("结果是：{0}".format(rst))
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

# 越具体的错误越往前放，越模糊的错误越往后放
# 捕获一个异常后，直接跳出下个代码块
