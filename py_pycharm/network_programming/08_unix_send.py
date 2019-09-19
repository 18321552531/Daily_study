# -*- coding: utf-8 -*-
# @Time    : 2019-09-19  13:19
# @File    : 08_unix_send.py
# @Author  : 啊啊

"客户端"
from socket import *
import os

sock_file = './sock_file'
# 确保文件两端用的同一个套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)

# 连接另一端
sockfd.connect(sock_file)

# 消息的收发
while True:
    # 写入消息
    message = input('>>')
    if message:
        sockfd.send(message.encode())
        print(sockfd.recv(1024).decode())
    else:
        break
sockfd.close()


