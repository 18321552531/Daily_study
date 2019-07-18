# -*- coding: utf-8 -*-
# @Time    : 2019-07-13  16:04
# @File    : 1.错误处理.py
# @Author  : 啊啊
'''
第一节 错误处理
什么是栈呢 ？？？
'''
'''
try.....except.....finally
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，
则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
'''

# try:
#     print('try....')
#     r = 10 / 3
#     print('result:', r)
# except ValueError as error:
#     print('ValueError:', error)
# except ZeroDivisionError as error:
#     print('except:', error)
# else:
#     print('No Error!')
# finally:
#     print('finally...')

'''
使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
这时，只要main()捕获到了，就可以处理：
'''
# def foo(s):
#     return 100/int(s)
#
# def bar(s):
#     return foo(s) * 5
#
# def main(s):
#     try:
#         print('try....')
#         bar(s)
#         print('result:', bar(s))
#     except ValueError as error:
#         print('ValueError:', error)
#     except ZeroDivisionError as error:
#         print('except:', error)
#     finally:
#         print('finally....')
#
# main(2)

'''
# 记录错误
# 见error_logging.py文件
'''

'''
# 抛出错误
'''

from functools import reduce

def str2num(s):
    # new_s = s.split('.')[0]
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()


