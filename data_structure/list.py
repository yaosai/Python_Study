#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: list.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/11 9:59
# @desc: list结构练习

a = [1, 2, 3, 4, 5, 6, 7]
print(id(a))

# 删除数组元素
del a[2]
print(a)
print(id(a))
# 可以看到，列表删除后没存地址不变
del a

# 列表相加
# 加号连接两个列表
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = a + b
print(c)

# 列表相乘
d = a * 3
print(d)

# 判断元素存在:in & not in
x = 4
print(x in a)
print(x not in a)

# 遍历
print(list(range(1, 10)))

# 双层列表循环
aa = [["one", 1], ["two", 2], ["three", 3]]
# 特例！解包的变量个数需与循环的参数一致
for k, v in aa:
    print(k, "---", v)

# list connect
# 快速生成新列表同时对列表操作
bb = ['a', 'b', 'c']
cc = [i for i in bb]
print(cc)

# 对bb中所有数乘10
bb = [1, 2, 3, 4, 5]
cc = [i * 10 for i in bb]
print(cc)

# 生成aa,将aa中所有偶数放入bb
aa = [x for x in range(1, 35)]
bb = [y for y in aa if y % 2 == 0]
print(bb)

# 列表常用函数
print(len(a))
print(max(a), min(a))

s = "i love python"
print(list(s))

a.append(111)
print(a)

# insert(index,data)
a.insert(2, 10)
print(a)
