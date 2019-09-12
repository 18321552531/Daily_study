#.-*-codeing:.utf-8 .-*-
#._Author_.="Zsz_aa"
#.Date:2019/9/12
'''
threadlocal
'''

import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print(f'Hello, {std} is in {threading.current_thread().name}')

def process_thread(name):
    local_school.student = name
    process_student()

s1 = threading.Thread(target=process_thread, args=('alice',), name='thread-a')
s2 = threading.Thread(target=process_thread, args=('bob',), name='thread-b')

s1.start()
s2.start()
s1.join()
s2.join()


