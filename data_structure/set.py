#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: set.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/11 14:11
# @desc: 集合练习

s = set()
print(type(s))

# 大括号内必须有值，否则定义的是dict
s = {}
print(type(s))
s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

# 集合无序，数据唯一，所以无法索引和切片
# 集合序列操作
s = {1, 2, 3, "hahaha", "www"}
i = "hahaha"
if i in s:
    print(i)
print(s)

# 集合遍历操作
for i in s:
    print(i, end=" ")
print()

# 带有元组的集合遍历
s = {(1, 2, 3), ("a", "b", "c"), (5, 6, 7)}
for k, v, m in s:
    print(k, "--", v, "--", m)

# 重复元素自动过滤
s = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}
print(s)

# copy拷贝
# remove移除指定的值，直接改变原有值，如果删除的值不在，报错
# discard移除指定集合的值，但不会报错
print("-" * 20)
s = {12, 342, 254, 31}
s.remove(12)
print(s)
s.discard(342)
print(s)
s.discard(100)
print(s)

# 集合函数
print("#" * 30)
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}
# 取交集
s_1 = s1.intersection(s2)
# 取差集
s_2 = s1.difference(s2)
# 取并集
s_3 = s1.union(s2)
# 检查是否是子集
s_4 = s1.issubset(s2)
# 检查是否是超集
s_5 = s1.issuperset(s2)
print(s_1)
print(s_2)
print(s_3)
print(s_4)
print(s_5)

# frozen set:冰冻集合,一种特殊集合，不能修改
# 创建
s = frozenset()
