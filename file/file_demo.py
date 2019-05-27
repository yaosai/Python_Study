#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: file_demo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/21 21:07
# @desc: 文件操作

import pickle as p

file_dir = 'D:\PythonProjects\study\\file.txt'
# r表示不需要转义
# 以追加方式打开文件，如果没有就创建
f = open(file_dir, 'a')
f.close()

# with语句：上下文管理协议
# 自动判断文件的作用域，自动关闭未使用的文件
# 按行读
with open(file_dir, 'r', encoding='UTF-8') as f1:
    # strline = f1.readline()
    # while strline:
    #     print(strline)
    #     strline = f.readline()
    # 用list代替f1.readline()
    l = list(f1)
    for line in l:
        print(line)

# 按字符读
with open(file_dir, 'r', encoding='UTF-8') as f2:
    strChar = f2.read()
    print(len(strChar))
    print(strChar)

# 序列化
a = [21, "yaosai", "java"]
with open(r"D:\PythonProjects\study\pickle.txt", 'wb') as f3:
    p.dump(a, f3)

# 反序列化
with open(r"D:\PythonProjects\study\pickle.txt", 'rb') as f4:
    a1 = p.load(f4)
    print(a1)
