# -*- coding: utf-8 -*-
# @Time    : 2019-09-26  22:51
# @File    : multiprocessing_1.py
# @Author  : 啊啊

import multiprocessing as mp
import time

a = 1

def fun_1():
    global a
    a = 19
    print(f'a={a}')
    time.sleep(3)
    print('I am fun1')

def fun_2():
    time.sleep(4)
    print('I am fun2')

p = mp.Process(target=fun_1)

start_time = time.time()
# 启动进程
p.start()

time.sleep(5)
print('this is parent fun')
# 回收进程
p.join()
print(time.time()-start_time)
print('parent a is ',a)




