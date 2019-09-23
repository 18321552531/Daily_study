# -*- coding: utf-8 -*-
# @Time    : 2019-09-23  12:59
# @File    : 09_fork_test.py
# @Author  : 啊啊


import os
import time

start_time = time.time()
def fun1():
    time.sleep(3)
    return print('fun1 end')

def fun2():
    time.sleep(4)
    return print('fun2 end')

pid = os.fork()

if pid<0:
    print('error pid')
elif pid == 0:
    fun1()
else:
    fun2()
end_time = time.time()
print(f'delta time is {end_time-start_time}')
print('run end')





