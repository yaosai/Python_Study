#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: p03.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/18 23:24
# @desc: 模块管理练习03


import sys

# sys.path存放所有包路径
print(type(sys.path))
print(sys.path)

for p in sys.path:
    print(p)

# 添加搜索路径
sys.path.append("path")


