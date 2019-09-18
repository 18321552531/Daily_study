# -*- coding: utf-8 -*-
# @Time    : 2019-09-18  21:49
# @File    : 07_select_server.py
# @Author  : 啊啊

from select import select
from socket import *

# 创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(10)

rlist = [s, ]
wlist = []
xlist = [s, ]

# 提交监测我们关注的IO等待IO发生
while True:
    rs,ws,xs = select(rlist, wlist, xlist)
    print('有IO事件发生')
    for r in rs:
        if r is s:
            c, addr = r.accept()
            rlist.append(c)
            print('connect from', addr)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                r.send(b'recv you messege!')

    for w in ws:
        pass
    for x in xs:
        pass



