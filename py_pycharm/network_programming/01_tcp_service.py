# -*- coding: utf-8 -*-
# @Time    : 2019-09-14  16:04
# @File    : 01_tcp_service.py
# @Author  : 啊啊

from socket import *

# 1.创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 设置端口立即释放
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 2.绑定地址
sockfd.bind(('0.0.0.0', 8803))


# 3.设置接听
sockfd.listen(10)

while True:
    # 4.等到接受连接
    print('waiting connect')
    connfd, addr = sockfd.accept()
    print('connect it')

    while True:
    # 5.收发消息
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(f'{addr} 向你发送消息{data}')
        return_data = input("你要返回什么消息").encode()
        n = connfd.send(return_data)
        print(f'发送了{n}字节')

    # 6.关闭套接字
    connfd.close()
sockfd.close()
print('服务端已退出！')




