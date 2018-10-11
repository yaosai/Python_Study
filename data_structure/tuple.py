#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: tuple.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/11 13:56
# @desc: 元组练习

# 元组可看做不可更改的list
# 创建空元组
t = ()
print(type(t))

# 传建一个元素元组，需要加","，否则计算机识别为int
t = (1,)

# 传建多元素元组
t = 1, 2, 3, 4, 5
print(type(t))

# 将list转tuple
l = [1, 2, 3]
t1 = tuple(l)
print(type(t1))

# 元组是有序的，可访问，不可修改
# 除了不可修改操作，tuple具有list的所有操作

# 索引
print(t[2])

# 切片
print(t[1:3])

# 序列相加
t1 = (1, 2, 3)
print(id(t1))
t2 = (4, 5, 6)
t1 = t1 + t2
print(t1)
print(id(t1))
# 为何可以相加？因为加操作并未修改元组，而是修改了t1的指向地址

# 元组遍历
for i in t:
    print(i, end=" ")
