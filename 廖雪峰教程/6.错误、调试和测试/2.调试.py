# -*- coding: utf-8 -*-
# @Time    : 2019-07-13  19:43
# @File    : 2.调试.py
# @Author  : 啊啊
'''
第二节 调试

pycharm调试？？？？？以后的重点
'''

'''
第一种简单粗暴，直接用print，将每个变量打印出来看看。
略
'''
###
'''
第二种方法是断言
凡是能用print的地方都能用assert进行断言。
'''
def foo(s):
    s = int(s)
    assert s != 0,'s is zero!'
    return 10 / s

def main(s):
    foo(s)

# main('0')

'''
第三种方法是
把print替换为logging，和assert相比logging不会
'''

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)



'''
第四种方法是使用python的调试器pdb，让程序以单步的方式运行，
'''


