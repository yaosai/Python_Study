#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: function_custom.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/10 18:10
# @desc: 自定义函数demo


def my_function(x):
    """
    自定义函数
    """
    if x >= 50:
        return x
    else:
        return -x


print(my_function(100))
print(my_function(15))


def nop():
    """
    定义空函数，使用pass，可表示暂时什么都不做
    """
    pass


# 九九乘法表
# for row in range(1, 10):
#     for col in range(1, row + 1):
#         print(row * col, sep="/t", end=" ")
#     print("-------------")


# 九九乘法表2.0
def printline(row):
    for col in range(1, row + 1):
        print(row * col, end=" ")
    print("")


for row in range(1, 10):
    printline(row)


# 收集参数，以*开头，参数具体内容不清楚
def stu(*args):
    print("hello，大家好")
    print(type(args))
    for item in args:
        print(item)


stu("aaa", 18, "北京人", "play game")
stu("bbb")


# 关键字收集参数
def stu_kw(**kwargs):
    print("hello！大家好")
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, "---", v)


stu_kw(name="gg", age=18, addr="北京")
print("*" * 20)
stu_kw(name="mm", age=24)
