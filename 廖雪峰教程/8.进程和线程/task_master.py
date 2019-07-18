# -*- coding: utf-8 -*-
# @Time    : 2019-07-17  10:59
# @File    : task_master.py
# @Author  : 啊啊

# 服务器进程
import random, time, queue
from multiprocessing.managers import BaseManager

## 发送任务的队列
task_queue = queue.Queue()
## 接受任务的队列
result_queue = queue.Queue()

# 从BaseManager继承Queuemanager
class QueueManager(BaseManager):
    pass

# 注册到网上
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口为500，验证码为‘abc’
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动queue
manager.start()
# 获取通过网络访问的对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 设置任务
for i in range(10):
    n = random.randint(0, 10000)
    print('put task %d...' % (n))
    task.put(n)
# 从result读取结果
print('get result...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result:%s' % r)
    print('result:%s' % r)
# 关闭
manager.shutdown()
print('结束进程！')


