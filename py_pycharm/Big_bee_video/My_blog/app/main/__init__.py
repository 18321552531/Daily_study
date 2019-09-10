# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  21:59
# @File    : __init__.py.py
# @Author  : 啊啊

'''
对main里面的业务逻辑进行初始化操作
'''
'''
通过蓝图
'''
# 导入蓝图
from flask import Blueprint
main_view = Blueprint('main_view', __name__)
from . import views
