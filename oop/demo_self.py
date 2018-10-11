#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: demo_self.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/11 18:15
# @desc: self理解


class A():
    name = "a"
    age = 18

    def __init__(self):
        self.name = "aaa"
        self.age = 19

    def say(self):
        print(self.name)
        print(self.age)


class B():
    name = "bbb"
    age = 20


a = A()
a.say()

# 此时，self被a替换
A.say(a)
# 此时，访问A的对象
A.say(A)
# 因为B具有name和age，所以不会报错(鸭子模型)
A.say(B)
