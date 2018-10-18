#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: p01.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/16 23:57
# @desc: 模块管理练习01


class Student():
    def __init__(self, name="yaosai", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))


def sayHello():
    print("Hello")


# if __name__ == '__main__'：
# 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
if __name__ == '__main__':
    print("hello everybody")
