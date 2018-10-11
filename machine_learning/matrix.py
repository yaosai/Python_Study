#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: matrix.py.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/11 1:09
# @desc: 机器学习实战demo，仅做了解

# 导入num包py
from numpy import *

# 生成4*4随机数组
print(random.rand(4, 4))

# mat函数将数组转为矩阵
randMat = mat(random.rand(4, 4))
print(randMat)

# randMat.I
# I操作符实现了矩阵求逆的运算
invRandMat = randMat.I
print(invRandMat)

# 将矩阵和其逆矩阵相乘
# 结果是单位矩阵,除了对角线元素是1,4x4矩阵的其他元素应该全是0。
# 实际输出结果略有不同,矩阵里还留下了许多非常小的元素,这是计算机处理误差产生的结果
myEye = randMat * invRandMat
print(myEye)

# 输入下述命令,得到误差值
print(myEye - eye(4))
