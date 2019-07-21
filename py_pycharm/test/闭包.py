# -*- coding: utf-8 -*-
# @Time    : 2019-07-21  22:15
# @File    : 闭包.py
# @Author  : 啊啊
def outer_func():
    loc_var = "local variable"
    def inner_func():
        # global loc_var
        loc_var += " in inner func"
        return loc_var
    return inner_func

clo_func = outer_func()
print(clo_func())

def get_select_desc(name, flag, is_format = True):

    if flag:
        sel_res = 'Do select name = %s' % name
    return sel_res if is_format else name

# get_select_desc('Error', False, True)