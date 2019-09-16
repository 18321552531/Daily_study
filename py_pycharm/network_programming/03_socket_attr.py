# -*- coding: utf-8 -*-
# @Time    : 2019-09-16  20:06
# @File    : 03_socket_attr.py
# @Author  : 啊啊

'''
了解一下套接字的属性：
'''

from socket import *

s = socket()

# s.family 获取套接字地址族类型
# 表示地址族用的是AF_INET
print(s.family)

# s.type 获取套接字类型
print(s.type)

# s.fileno()获取文件描述符
print(s.fileno())

# s.getpeername()客户端连接套接字

print(gethostbyname('zhushengzudeMacBook-Pro.local'))

