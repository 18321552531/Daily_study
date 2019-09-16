# -*- coding: utf-8 -*-
# @Time    : 2019-09-16  13:06
# @File    : 02_udp_client.py
# @Author  : 啊啊

from socket import *
import sys

# 命令行输入端口
host = sys.argv[1]
post = sys.argv[2]
addr = (host, int(post))

# 1.创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 2.消息的收发
while True:
    data = input("输入发送消息:")
    if not data:
        break
    sockfd.sendto(data.encode(), addr)
    data, addr = sockfd.recvfrom(1024)

# 3.关闭
sockfd.close()



