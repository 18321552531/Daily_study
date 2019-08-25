# -*- coding: utf-8 -*-
# @Time    : 2019-08-25  21:54
# @File    : nonlocal.py
# @Author  : 啊啊

'''
nonlocal函数
    作用：告诉解释器，nonlocal变量不是局部变量，也不是全局变量，
    外部嵌套函数内的变量
'''

'''
nonlocal 只能在被嵌套函数内部使用。
'''

var = 100
def fn():
    # global var
    var = 200
    print('fn里面的var为%s'%(var))
    def f2():
        nonlocal var
        var = 300
        print('f2里面的var为%s'%(var))
    f2()
    print('f2调用结束后var的值为%s'%(var))

fn()
print(var)

