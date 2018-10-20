#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: shutil_demo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/20 21:44
# @desc: 归档和压缩


import shutil as sh
import zipfile
import random

# 将common包的内容进行归档操作
rst = sh.make_archive("D:\PythonProjects\study\common", "zip", "D:\PythonProjects\study\common")

# 解包函数
# sh.unpack_archive()

# 创建一个ZipFile对象，表示一个zip文件
zf = zipfile.ZipFile("D:\PythonProjects\study\common.zip")
print(zf)

# getinfo()获取压缩对象内指定的文件信息，
zf_info = zf.getinfo("os_demo.py")
print(zf_info)

# 打印压缩包所有文件
print(zf.namelist())

# 返回一个随机数
print(random.random())

# 从一个数组里随机取值
print(random.choice([i for i in range(1, 100)]))
