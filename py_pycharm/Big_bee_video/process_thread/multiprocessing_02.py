# -*- coding: utf-8 -*-
# @Time    : 2019-09-26  23:26
# @File    : multiprocessing_02.py
# @Author  : 啊啊
from multiprocessing import Process
import time
import os

def th1():
    time.sleep(5)
    print('eating -----')
    print(os.getppid(),'------',os.getpid())


def th2():
    time.sleep(6)
    print('sleeping -----')
    print(os.getppid(),'------',os.getpid())


def th3():
    time.sleep(4)
    print('fighting -----')
    print(os.getppid(),'------',os.getpid())


things = [th1,th2,th3]
process = []

start_time = time.time()
for th in things:
    p = Process(target=th,)
    process.append(p)
    p.start()

for i in process:
    i.join()
print(f'use {time.time() - start_time} second')