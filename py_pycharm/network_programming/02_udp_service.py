# -*- coding: utf-8 -*-
# @Time    : 2019-09-16  12:59
# @File    : 02_udp_service.py
# @Author  : 啊啊
from socket import *

# 1.创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 2.绑定服务端地址
sockfd.bind(('0.0.0.0', 8804))

# 3.收发消息
while True:
    print('waiting to connect')
    data,addr = sockfd.recvfrom(1024)
    print(f'recive from {addr} data is {data.decode()}')
    sockfd.sendto('i have recieve you messege'.encode(), addr)

# 4.接收消息
sockfd.close()




