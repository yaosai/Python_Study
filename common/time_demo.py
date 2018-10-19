#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: time_demo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/19 18:14
# @desc: 时间戳包


import time

# 打印当前时区和UTC时间相差的秒数
print(time.timezone)
# 得到当前的时间结构
t = time.localtime()
print(t)
# 打印当前小时
print(t.tm_hour)
# 将当前时间格式化,是str类型
tt = time.asctime()
print(tt)

# 根据当前时间元组，返回浮点类型时间戳
ts = time.mktime(t)
print(ts)

# 睡眠1秒
time.sleep(1)

# 直接打印会报错！！！
y = "%Y{0}%m{1}%d{2} %H:%M"
print(y)
str = time.strftime(y, t)
print(str.format("年", "月", "日"))
