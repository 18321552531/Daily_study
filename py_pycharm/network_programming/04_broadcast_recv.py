# -*- coding: utf-8 -*-
# @Time    : 2019-09-16  20:53
# @File    : 04_broadcast_recv.py
# @Author  : 啊啊

from socket import *
import time

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 设置套接字可以发送接收广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# 绑定固定接收端口
sockfd.bind(('0.0.0.0', 9999))

while True:
    try:
        print('尝试接收消息')
        msg,addr = sockfd.recvfrom(1024)
        print(f'从{addr}获取信息{msg.decode()}')

    except (KeyboardInterrupt,SyntaxError):
        print('出错了')
        raise
    except Exception as e:
        print(e)

sockfd.close()

