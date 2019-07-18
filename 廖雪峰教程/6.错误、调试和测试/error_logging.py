# -*- coding: utf-8 -*-
# @Time    : 2019-07-13  16:41
# @File    : error_logging.py
# @Author  : 啊啊


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 100

def main(s):
    try:
        print('try...')
        bar(s)
        print('result:', bar(s))
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main(0)
    print('end')

