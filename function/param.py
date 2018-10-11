#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: param.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/10 22:25
# @desc: 函数参数练习


# 默认参数练习
# 函数在传入时已经定义了一个默认值
def func_d(name, age, sex="man"):
    if sex == "man":
        print("你好！{0}岁的男生{1}！".format(age, name))
    else:
        print("你好！{0}岁的女生{1}！".format(age, name))


func_d("gg", 24, "man")
func_d("mm", 18, "woman")
