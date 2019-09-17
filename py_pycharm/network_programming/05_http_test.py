# -*- coding: utf-8 -*-
# @Time    : 2019-09-17  13:16
# @File    : 05_http_test.py
# @Author  : 啊啊

from socket import *

# 创建tcp套接字
sockfd = socket()

# 绑定
sockfd.bind(('0.0.0.0',8889))
sockfd.listen(5)

while True:
    print('waiting connecting')
    connfd, addr = sockfd.accept()
    print(f'connect from {addr}')
    data = connfd.recv(10240)
    resend = '''HTTP/1.1 200 OK
    Content-Encoding: gzip
    Content-Type: text/html

    <h1>hello</h1>
    '''
    data2 = '''HTTP/1.1 200 OK
    Content-Encoding: gzip
    Content-Type: text/html

    <h1>Welcome to tedu</h1>
    <p>这是一个测试</p>
    '''
    connfd.send(resend.encode())
    connfd.close()

sockfd.close()


