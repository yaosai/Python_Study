#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: function_magic.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/15 22:49
# @desc: 魔法函数练习


# 魔法函数，不用执行，在特定的时候会被调用
class A():

    # 操作类：
    # __init__,初始化
    def __init__(self):
        print("hahaha")

    # __call__对象当函数调用时自动调用此方法，若无此方法报错
    def __call__(self, *args, **kwargs):
        print("again")

    # 常用魔法函数还有__str__,此方法作用同java中toString
    def __str__(self):
        return "toString"


# a是一个实例化A的一个对象
a = A()
# a后面跟()，此写法即是将对象当函数调用
a()
print(a)


# __getattr__方法，get的参数不存在时调用
class B():
    name = "yao"
    age = 18

    def __getattr__(self, item):
        print("NoThing")


b = B()
print(b.name)
print(b.test)


class C():
    def __setattr__(self, key, value):
        print("hahaha")
        # 当语句赋值时会调用__setattr__,下面语句会赋值，会导致死循环
        # self.key = value
        # 解决方法：调用父类方法
        super().__setattr__(key, value)


c = C()
c.age = 18


# 运算相关魔术方法
# __gt__:进行大于判断时执行的函数
class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, other):
        print("{0}比{1}大么".format(self, other))
        return self._name > other._name

    def __str__(self):
        return self._name


stu1 = Student("one")
stu2 = Student("two")

print(stu1 > stu2)
