# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  22:03
# @File    : views.py
# @Author  : 啊啊


'''
用户模块中的视图和路由定义
'''

from flask import render_template
from . import user
from ..models import *
from .. import db


@user.route('/user',)
def user():
    return '这是user的主页'

