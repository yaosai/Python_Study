#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: p01.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/16 23:57
# @desc: 包练习


class Student():
    def __init__(self, name="yaosai", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))


def sayHello():
    print("Hello")


print("hello everybody")
