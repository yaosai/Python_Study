#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: demo_encapsulation.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/12 0:02
# @desc: 封装练习


class Person():
    # name是公有变量public
    name = "lilei"
    # age是私有变量private
    # python的私有不是真正的私有，是一种改名的策略，外部访问不到是因为变量名不是__开头了
    __age = 18


p = Person()
print(p.name)
print(Person.__dict__)
# 按照_className__attributename格式可以访问，但不推荐
print(p._Person__age)


# 受保护的封装protected
# 在类和子类中都可以访问，但在外部不可以
# 在成员名称前加一个下划线即可


# class Teacher():
#     # name是公有变量public
#     name = "lilei"
#     # age是私有变量private
#     # python的私有不是真正的私有，是一种改名的策略，外部访问不到是因为变量名不是__开头了
#     _age = 18
#     __score = 100

