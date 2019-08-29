#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: decorators_01.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-28 21:55:37
##########################################
import logging
import time 
import functools
'''
装饰器的介绍（专业提高篇）
'''

# 打印函数运行时间的装饰器

def print_time(func):
    def fx(*args,**kw):
        start_time = time.time()
        func()
        end_time = time.time()
        print('总共用了%s秒.'%(end_time-start_time))
    return(fx)

@print_time
def run_func():
    print('开始执行！')
    time.sleep(3)
    print('结束执行！')


# 廖雪峰教程

def log(func):
    functools.wraps(func)
    def wrapper(*args,**kw):
        print('开始执行%s函数！'%(func.__name__))
        start_time = time.time()
        func()
        end_time = time.time()
        print('结束执行%s函数'%(func.__name__))
        print('函数的执行时间为%s秒'%(end_time-start_time))
    return wrapper

@log
def my_fun():
    print('开始执行！')
    time.sleep(3)
    print('结束执行！')


my_fun()

