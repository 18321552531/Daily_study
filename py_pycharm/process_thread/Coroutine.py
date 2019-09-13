# -*- coding: utf-8 -*-
# @Time    : 2019-09-12  22:36
# @File    : Coroutine.py
# @Author  : 啊啊


def consumer():
    r = ''
    while True:
        n = yield r
        # if not n:
        #     return
        print(f'[comsumer] consuming {n} ')
        r = '200ok'

def produce(c):
    c.send(None)
    n = 0
    while n<6:
        n += 1
        print(f'[produce] producing {n}')
        r = c.send(n)
        print(f'[produce] custmer return: {r}')

    c.close()

c = consumer()
produce(c)



