#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: calendar_demo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/19 18:02
# @desc: Calendar模块练习（日历类）


import calendar

cal = calendar.calendar(2018)

print(type(cal))
# 打印日历
print(cal)
# 判断某一年是否是闰年
print(calendar.isleap(2018))
# 获取区间内的闰年个数
print(calendar.leapdays(1998, 2008))
# 打印月
print(calendar.month(2018, 3))

print(calendar.monthrange(2018, 3))
# 返回矩阵
print(calendar.monthcalendar(2018, 10))
# 直接打印一年日历
calendar.prcal(2018)
# 打印月份日历
calendar.prmonth(2018, 3)
