# -*- coding: utf-8 -*-
# @Time    : 2019-09-19  13:19
# @File    : 08_unix_recv.py
# @Author  : 啊啊

"服务端"
from socket import *
import os

# 创建套接字文件
sock_file = './sock_file'
# 判断文件是否存在
if os.path.exists(sock_file):
    os.remove(sock_file)

# 创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)
# 绑定套接字文件
sockfd.bind(sock_file)
#监听
sockfd.listen(10)
print('perpare receive')
# 消息收发
while True:
    conn,addr = sockfd.accept()
    data = conn.recv(1024)
    if data:
        print(f"data is {data.decode()}")
        conn.send(b'i receive it')
    else:
        break
    conn.close()

sockfd.close()
