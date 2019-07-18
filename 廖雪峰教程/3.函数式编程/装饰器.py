# -*- coding: utf-8 -*-
# @Time    : 2019-07-07  22:32
# @File    : 装饰器.py
# @Author  : 啊啊
'''
装饰器（decorater）：感觉上这个很重要啊
函数是一个对象，函数可以赋值给一个对象，也能通过变量调用该函数。
'''
import datetime

def now_time():
    return print(datetime.datetime.now())

# print(now_time.__name__)
'''
# 增强now函数的功能，在调用前后自动打印日志，且不改变now函数的定义。
# decorater本质上是个返回函数的高阶函数。
其函数如下：
'''
# def log(function):
#     def wrapper(*args, **kwargs):
#         print('执行：%s' % (function.__name__))
#         return function(*args, *kwargs)
#     return wrapper
#
# @log
# def now():
#     return print('现在的时间是：%s' % (datetime.datetime.now()))
#
# time = now()
# 假如decorator本身要传入参数，则要在编写一个返回decorator的函数



#------------------new-------------------
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kwargs):
            print('%s: %s' % (text, func.__name__))
            return func(*args, **kwargs)
        return wapper
    return decorator

@log('开始执行')
def get_nowtime():
    return print('现在的时间是：%s' % (datetime.datetime.now()))

get_nowtime()
print(get_nowtime.__name__)

# 打印函数的执行时间
import time
def metric(func):
    @functools.wraps(func)
    def wapper(*args, **kwargs):
        start_time = time.time()
        print('%s开始运行。' % (func.__name__))
        func(*args, **kwargs)
        print('%s结束运行。' % (func.__name__))
        end_time = time.time()
        print('函数执行的时间为：%s' % (end_time - start_time))
        return func(*args, **kwargs)
    return wapper

@metric
def test_fun(a, b, c):
    time.sleep(2)
    return a + b + c

num = test_fun(2, 4, 56)
print(num)



