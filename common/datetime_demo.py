#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: datetime_demo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/19 22:33
# @desc: 日期和时间的运算表示

import datetime

import timeit

print(datetime.datetime(2018, 10, 19, 22, 35, 34))
dt = datetime.datetime(2018, 10, 19, 22, 35, 34)
dd = datetime.date(2018, 10, 19)
print(dd.month)

# 将时间戳转为时间
print(dt.fromtimestamp(dt.timestamp()))

# 时间间隔timedelta
tn = datetime.datetime.now()
print(tn)
td = datetime.timedelta(hours=1)
print(tn + td)

# timeit方法测试程序运行时间
# stmt:表示执行代码段，是string类型
# number:表示执行次数
c = '''
sum=[]
for i in range(1000):
    sum.append(i)
'''
t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=10000)
t2 = timeit.timeit(stmt=c, number=10000)
print(t1)
print(t2)
