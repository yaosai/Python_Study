#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: time.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/11/1 17:35
# @desc: time函数
import time


def loop1():
    print(time.ctime())
    time.sleep(4)
    print(time.ctime())


def loop2():
    print(time.ctime())
    time.sleep(2)
    print(time.ctime())


def main():
    print(time.ctime())
    loop1()
    loop2()
    print(time.ctime())


if __name__ == '__main__':
    main()
