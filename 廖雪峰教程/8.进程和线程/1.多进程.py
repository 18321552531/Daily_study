# -*- coding: utf-8 -*-
# @Time    : 2019-07-14  21:18
# @File    : 1.多进程.py
# @Author  : 啊啊
'''
第一节 多进程（multiprocessing）
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，
返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
'''

'''
fork()
'''
import os
# print('Process %s start' % (os.getpid()))
#
# pid = os.fork()
# if pid == 0:
#     print('子进程为：%s ,父进程为：%s' % (os.getpid(), os.getppid()))
# else:
#     print('父进程为：%s' % (pid))


'''
muliprocessing
'''
import multiprocessing as mp
def run_processing(name):
    print('run child processing %s: %s' % (name, os.getpid()))

def print_hello(a,b):
    print('hello'+a+b)

'''
Pool 进行批量创建子进程
'''
import time, random

def long_time_task(name):
    print('Run task%s: %s'%(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f second.' % (name, os.getpid()))

if __name__ == '__main__':
    # process = mp.Process(target=run_processing, args=('ceshi', ))
    # print('start!')
    # process.start()
    # process.join()
    # print('end!')
    p = mp.Pool(5)
    for i in range(8):
        p.apply_async(long_time_task, args=(i, ))
    p.close()
    p.join()