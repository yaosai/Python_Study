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


# 继承中的构造函数
# 类被实例化时自动执行
class A():
    def __init__(self, name):
        print("A is {0}".format(name))


class B(A):
    def __init__(self):
        print("B is SSS")


b = B()


# 父类构造函数有参数，子类无构造参数，默认调用父类构造函数，需要传参
class C(A):
    pass


# 传参"hahaha"自动交由执行
c = C("hahaha")

# super不是关键字，而是一个类
# super是获取MRO列表中的第一个类，而这个类就是对象的父类
# 因此，super虽然不是父类，但是通过super可以调用到第一个类
# super使用两个方法
