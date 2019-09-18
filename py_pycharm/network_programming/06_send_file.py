# -*- coding: utf-8 -*-
# @Time    : 2019-09-18  13:39
# @File    : 06_send_file.py
# @Author  : 啊啊


'''
客户端
'''
from socket import *

# 创建套接字
sockfd = socket()
sockfd.connect(('localhost',8888))

f = open('send.jpg', 'rb')

while True:
    data = f.read(1024)
    sockfd.send(data)
    if not data:
        break

f.close()
sockfd.close()

#



