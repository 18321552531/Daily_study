# -*- coding: utf-8 -*-
# @Time    : 2019-09-12  11:21
# @File    : multiprocessing_test.py
# @Author  : 啊啊


import os
import multiprocessing as mp

# print(f'Process {os.getpid()} is start!')

# pid = os.fork()
# if pid == 0:
#     print('pid is 0')
# else:
#     print('pid is not 0')

# multiprocessing

# 子进程要执行的代码
def run_proc(name):
    print(f'run child process id {name},{os.getpid()}')

print('parent pid is %s'%os.getpid())
p = mp.Process(run_proc('test'))
print('child will start')
p.start()
p.join()
print('child is stop')
