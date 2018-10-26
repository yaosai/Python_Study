#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: log_demo.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/26 1:21
# @desc: log日志练习


import logging

LOG_FORMAT = "%(asctime)s-----%(levelname)s-----%(message)s"
logging.basicConfig(filename='D:\PythonProjects\study\myLog.log', level=logging.DEBUG, format=LOG_FORMAT)
logging.error("this is a error log")
logging.warning("this is a warning log")
logging.debug("this is a debug log")
logging.info("this is a info log")
logging.critical("this is a critical log")
