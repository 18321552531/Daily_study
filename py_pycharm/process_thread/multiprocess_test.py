#.-*-codeing:.utf-8 .-*-
#._Author_.="Zsz_aa"
#.Date:2019/9/12

'''
multiprocess
'''

# fork one time return two values
import os
# print(f'Process {os.getpid()}')
#
# pid = os.fork()
# print(pid)
# if pid == 0:
#     print(f'i am child process {os.getpid()} my parent is {os.getpid()}')
# else:
#     print(f'I {os.getpid()} just create a child process {pid}')

from multiprocessing import Process,Pool,Queue
import time,os,random
def run_proc(name):
    print(f'run child process {os.getpid()}')

def long_time_task(name):
    print(f'run task {name} {os.getpid()}')
    start = time.time()
    time.sleep(random.random()*2)
    end = time.time()
    print(f'Task {name} runs {end-start} seconds')

def write(thing):
    print(f'process to write {os.getpid()}')
    for value in ['A','B','C']:
        print(f'put {value} to queue')
        thing.put(value)
        time.sleep(random.random())

def read(thing):
    print(f'process to read{os.getpid()}')
    while True:
        value = thing.get(True)
        print(f'get {value} from queue')

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()