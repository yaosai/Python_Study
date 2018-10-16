#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @file: demo_abstract.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/16 22:39
# @desc: 抽象类


import abc


# 抽象类不允许实例化
# 声明一个抽象类并指定当前类的元类
class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass
