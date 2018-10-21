#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: filter_sorted.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/21 11:28
# @desc: filter过滤和sorted排序


def even(n):
    return n % 2 == 0


l = range(1, 10)

# 返回结果是一个可迭代的filter对象
print(filter(even, l))

print([i for i in filter(even, l)])

# 高阶函数 排序
l2 = [12, 23, 1, 24, 4, 67, -12, -100]

print(sorted(l2))


# 闭包
def myF1(*args):
    def myF2():
        sum = 0
        for i in args:
            sum += i
        return sum

    return myF2


myF3 = myF1(1, 2, 3, 4)
print(myF3())

# 闭包(closure)
# 返回闭包时，返回函数不能引用任何循环变量
