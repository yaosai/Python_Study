#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: pkg01.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/18 23:36
# @desc:


class Student():
    def __init__(self, name="yaosai", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))


def sayHello():
    print("Hello")


print("hello everybody")
