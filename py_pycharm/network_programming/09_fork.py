# -*- coding: utf-8 -*-
# @Time    : 2019-09-22  22:17
# @File    : 09_fork.py
# @Author  : 啊啊


import os,sys
import time


print('**************')
pid = os.fork()
a = 1

if pid<0:
    print('创建失败')
elif pid == 0:
    time.sleep(1)
    print('这是新的进程')
    print(f'child pid is {os.getpid()}')
    print(f'child get parent pid is {os.getppid()}')
    a = 1000
    try:
        sys.exit('程序退出')
    except SystemExit as e:
        print('error is', e)
else:
    print(f'parent pid child is {pid}')
    print(f'parent get is {os.getpid()}')
    print('这是原有进程')
    print('parent',a)
    os._exit(1)



print('*******end*****')






