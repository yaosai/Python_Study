#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: os_demo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/20 18:43
# @desc: os 操作系统相关

import os

# os模块(操作系统目录相关)、os.path模块(系统路径相关操作)、shutil模块(高级文件操作)
# 获取当前系统工作目录
print(os.getcwd())

# 改变当前工作目录
os.chdir("D:\PythonProjects\study")
print(os.getcwd())

# 遍历出当前目录下的所有文件
print(os.listdir())

# 递归创建文件夹
# print(os.makedirs("yaosai"))

# os模块执行系统命令，但一般使用subprocess模块代替
# os.system("ipconfig")

print("*" * 30)
# 值部分
# 打印当前目录
print(os.curdir)
# 打印父目录
print(os.pardir)
# 打印路径分隔符
print(os.sep)
# 打印当前系统换行符
print(os.linesep)

print(os.name)
