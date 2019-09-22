# -*- coding: utf-8 -*-
# @Time    : 2019-09-22  23:23
# @File    : 09_fork_chile.py
# @Author  : 啊啊

import os
import time

pid = os.fork()

if pid<0:
    print('can not create child pid')
elif pid == 0:
    print('i am a child pid')
else:
    print('i am a parent pid')
    while True:
        pass




