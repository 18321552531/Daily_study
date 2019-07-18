# -*- coding: utf-8 -*-
# @Time    : 2019-07-07  23:06
# @File    : 偏函数.py
# @Author  : 啊啊
'''
偏函数：
function.partail 的作用就是把原本函数的某些参数给固定性，
返回一个新的函数，使得函数的调用更加的简单

'''
import functools

#例如将十进制的字符串改为转化二进制的字符串
##1.第一种
def int2(n, base=2):
    return int(n, base=2)

print(int2('10010'))
int2_1 = functools.partial(int,base=2)
print(int2_1('10010'))


kw = {'base':2}
print(int('10010', **kw))