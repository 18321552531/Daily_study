# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  22:02
# @File    : __init__.py.py
# @Author  : 啊啊

'''
用户模块的初始化
'''

from flask import Blueprint
user = Blueprint('user', __name__)
from . import views
from ..models import *

