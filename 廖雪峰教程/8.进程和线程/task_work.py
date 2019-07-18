# -*- coding: utf-8 -*-
# @Time    : 2019-07-17  10:59
# @File    : task_work.py
# @Author  : 啊啊
import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

# 由于只从网上获取Queue所以注册的时候只要，提供名字：
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
server_add = '127.0.0.1'
print('正在连接：%s' % server_add)

# 端口验证
m = QueueManager(address=(server_add, 5000), authkey=b'abc')
m.connect()
# 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()
# 结果写入reslut
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task is empty!')
print('work exit!')





