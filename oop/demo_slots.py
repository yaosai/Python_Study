#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: demo_slots.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/12 9:30
# @desc: 


# 限制实例的属性,使用__slots__
# __slots__只对当前类有效，对子类无效
class Student():
    # 用tuple赋值
    __slots__ = ("name", "age")


s = Student()
s.name = "yaosai"
s.age = 18
