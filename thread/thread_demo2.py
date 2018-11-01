#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: thread_demo1.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/11/1 17:26
# @desc: thread练习

# 全局解释器锁（GIL）
# Python代码由python虚拟机运行,同一时间段只能有一个控制线程执行
from multiprocessing import Process
import os


# print('Process (%s) start...' % os.getpid())
# # 只能在Unix/Linux/Mac下运行
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 子进程执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
