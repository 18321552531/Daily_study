# -*- coding: utf-8 -*-
# @Time    : 2019-08-25  15:36
# @File    : global_local_var.py
# @Author  : 啊啊

'''
局部变量：
1.定义在函数内部的变量，只能在函数内部使用
2.只有在函数调用时才会被创建，结束后自动销毁
全局变量：
1.定义在函数外部，模块内部的变量，
2.所有的函数可以直接访问（但是函数内部不能将其直接赋值）
'''

a = 100
b = 200

def fn(c):
    global d
    d = 300
    a = 2
    dic_local = locals()
    print(dic_local)
    print(a,b,c,d)
dic_global = globals()
print(dic_global)
fn(9090)

'''
globals 和 locals
globals : 返回全局作用域内的字典
lobals：返回局部作用域内的字典
'''