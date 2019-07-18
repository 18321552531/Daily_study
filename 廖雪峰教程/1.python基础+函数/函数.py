# -*- coding: utf-8 -*-
# @Time    : 2019/6/26  下午11:30
# @File    : 函数.py
# @Author  : 啊啊

####第一节  调用函数
#hex()转化为16进制的函数
print(hex(255))

##定义函数 pass

##注意调用函数时候可以使用默认参数，重要的。
def enroll(name,city,age=6):
    print('名字是：', name)
    print('城市是：', city)
    print('年龄是：', age)

print(enroll('aa','shanghai',7))

def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())

##*args是可变参数，args接收的是一个tuple；
##**kw是关键字参数，kw接收的是一个dict：
####函数的参数
###例子定义一个函数的n次方

def power(x, n):
    s = 1
    if n>0:
        data = x ** n
    return data

def power1(x, n):
    s = 1
    for i in range(n):
        s = s*x
    return s

'''
递归函数的使用
即函数调用自身
'''
##例如计算阶乘
def fun(n):
    '''
    :param n:为大于0的整数
    :return:
    '''
    if n == 1:
        return 1
    else:
        return n*fun(n-1)

def recursive_fun(i):
    m=1
    for x in range(1,i+1):
        m = m*x
    return m
###尾递归
def fiter_fun(num, project):
    if num == 1:
        return project
    else:
        return fiter_fun(num-1, num*project)
"""
汉诺塔移动的实现：
解释：当n个盘子时候从A-->C,B为辅助的柱子，
则当n-1时候，A为辅助柱子
"""
def move(n,a,b,c):
    if n == 1:
        print(a, '--->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)





if __name__ == '__main__':
    # data = power1(3,4)
    # print(fun(6))
    # print(fiter_fun(6,1))
    # print(recursive_fun(6))
    move(3,'a','b','c')


