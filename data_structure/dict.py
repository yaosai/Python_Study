#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: dict.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/11 15:05
# @desc: 字典

d = {}

d = dict()

d = {"one": 1, "two": 2, "three": 3}
print(d)

# 字典是序列类型，但字典是无序序列，所以没有分片和索引
# 访问字典操作
print(d["one"])
# 赋值
d["one"] = "xxx"
print(d)
# 删除
del d["one"]
print(d)

# 遍历
for k in d:
    print(k, d[k])

for k in d.keys():
    print(k, d[k])
# 字典生成式
dd = {k: v for k, v in d.items() if v % 2 == 0}
print(dd)
