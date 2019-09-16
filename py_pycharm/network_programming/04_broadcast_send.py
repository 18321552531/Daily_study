# -*- coding: utf-8 -*-
# @Time    : 2019-09-16  21:02
# @File    : 04_broadcast_send.py
# @Author  : 啊啊

from socket import *
import time

# 设置目标地址
addr = ('172.20.10.255', 9999)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    time.sleep(2)
    print('开始发送')
    sockfd.sendto('come on, everything will be ok'.encode(),addr)

sockfd.close()





