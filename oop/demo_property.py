#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: demo_property.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/15 1:33
# @desc: 属性练习


class Person():
    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "属性练习测试")


p1 = Person()
p1.name = "study"
print(p1._name)
