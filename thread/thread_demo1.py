#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: thread_demo1.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/11/1 17:26
# @desc: thread练习

# 全局解释器锁（GIL）
# Python代码由python虚拟机运行,同一时间段只能有一个控制线程执行

import time
import _thread as thread


def loop1():
    print('start1', time.ctime())
    time.sleep(4)
    print('end1', time.ctime())


def loop2():
    print('start2', time.ctime())
    time.sleep(2)
    print('end2', time.ctime())


def main():
    print(time.ctime())
    thread.start_new_thread(loop1())
    thread.start_new_thread(loop2())
    print(time.ctime())


if __name__ == '__main__':
    main()
    # 死循环，等待线程结束
    while True:
        time.sleep(1)
