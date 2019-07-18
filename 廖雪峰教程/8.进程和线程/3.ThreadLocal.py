# -*- coding: utf-8 -*-
# @Time    : 2019-07-17  09:23
# @File    : 3.ThreadLocal.py
# @Author  : 啊啊
'''
threadlocal

'''
import threading

# 创建threading.local对象
local_school = threading.local()
def process_student():
    stu = local_school.student
    print('Hello %s(in %s)' % (stu, threading.current_thread().name))

def process_thead(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thead, args=('Bob',), name='Thread-A')
t2 = threading.Thread(target=process_thead, args=('sam',), name='Thread-B')

t1.start()
t2.start()

t1.join()
t2.join()



