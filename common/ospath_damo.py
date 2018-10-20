#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: ospath_damo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/20 20:28
# @desc: os.path模块练习(路径相关)

import os.path as op

# "."表示当前目录
# ".."表示父目录
# 获取当前文件路径
absp = op.abspath(".")
print(absp)

# basename获取路径中文件名部分
bn = op.basename("D:\PythonProjects\study")
print(bn)

# join方法，传入两个路径自动拼接新路径
bd = "D:\PythonProjects\study"
fn = "common"
print(op.join(bd, fn))

# 将文件切割为文件和路径
print(op.split("D:\PythonProjects\study"))

# 判断是否是目录
print(op.isdir("D:\PythonProjects\study"))

