#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: demo_inheritance.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/12 0:16
# @desc: 继承练习


# Teacher继承了Person，拥有Person的read方法，自身拥有run方法
class Person():
    def read(self):
        print("read book")


class Teacher(Person):
    def run(self):
        print("running")


t = Teacher()
t.read()
t.run()

a = list()
b = Person()
c = Teacher()
# isinstance方法判断某个变量是否是某个类型
print(isinstance(a, list))
print(isinstance(b, Person))
print(isinstance(c, Teacher))
print(isinstance(c, Person))
