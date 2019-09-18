# -*- coding: utf-8 -*-
# @Time    : 2019-09-14  16:37
# @File    : 01_tcp_client.py
# @Author  : 啊啊

from socket import *

# 1.创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)

# 2.发起连接
sockfd.connect(('127.0.0.1', 8888))

while True:
# 3.消息收发
    data = input('输入消息：')
    sockfd.send(data.encode())
    if not data:
        break
    recv_data = sockfd.recv(1024)
    print(f'接收到的消息是：{recv_data.decode()}')

# 4.关闭套接字

sockfd.close()
print('客户端已退出！')






