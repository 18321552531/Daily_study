# -*- coding: utf-8 -*-
# @Time    : 2019-09-18  13:40
# @File    : 06_recv_file.py
# @Author  : 啊啊

'''
服务端
'''

from socket import *

# 创建套接字
sockfd = socket()
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(10)

# 接受连接
connfd, addr = sockfd.accept()

print('已经连接')
# 接收文件
with open('test.jpg', 'wb') as f:
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        f.write(data)

connfd.close()
sockfd.close()





