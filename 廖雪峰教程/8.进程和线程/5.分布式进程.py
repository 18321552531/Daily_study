# -*- coding: utf-8 -*-
# @Time    : 2019-07-17  10:28
# @File    : 5.分布式进程.py
# @Author  : 啊啊

'''
第五节 分布式进程
将多进程分布到多台计算机上
python的multiprocessing模块不但支持多进程，其子模块managers支持将多进程分步到多台计算机上。
'''

'''
如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，
由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
'''
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