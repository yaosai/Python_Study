#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: threading.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/11/1 18:08
# @desc: 
import threading


def run_proc(name):
    print('Run child process %s (%s)...' % (name,))


t = threading.Thread(target=run_proc, args=('name',))
# 线程执行
t.start()
# 等待多线程执行完成
t.join()
