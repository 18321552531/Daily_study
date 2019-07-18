# -*- coding: utf-8 -*-
# @Time    : 2019-07-16  23:33
# @File    : 2.多线程.py
# @Author  : 啊啊
import threading, time

def loop():
    print('threading %s is running!' % threading.current_thread())
    n = 0
    while n <= 5:
        n += 1
        print('threading %s is running!' % threading.current_thread(), n)
        time.sleep(1)
    print('threading %s is ending!' % threading.current_thread())


# print('threading %s is running!' % threading.current_thread())
# t = threading.Thread(target=loop, )
# t.start()
# t.join()

'''
多线程会改乱变量
'''

balance = 0 #你的余额
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    return balance

def run_threading(n):
    for i in range(1000000):
        change_it(n)


t1 = threading.Thread(target=run_threading, args=(8,))
t2 = threading.Thread(target=run_threading, args=(6,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)