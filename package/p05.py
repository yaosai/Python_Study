#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: p05.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/18 23:37
# @desc: 包练习：导入模块


import pkg01.pkg01

stu = pkg01.pkg01.Student()
stu.say()

# 此种导入方法不执行__init__
# from pkg01 import pkg01

# 此种导入方法只导入__init__模块
# from pkg01 import *

# 此种导入方法导入指定模块中的所有内容
# from pkg01.pkg01 import *

# __all__的用法
# __all__不是函数,导入时按照__all__中内容导入
