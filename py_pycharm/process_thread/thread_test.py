#.-*-codeing:.utf-8 .-*-
#._Author_.="Zsz_aa"
#.Date:2019/9/12

import time,threading

def loop():
    print(f'thread {threading.current_thread().name} is running ')
    n=0
    while n < 4:
        n += 1
        print(f'thead {threading.current_thread().name} ===> {n}')
        time.sleep(2)
    print(f'thread {threading.current_thread().name} is end')

balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    lock = threading.Lock()
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(8,))
t2 = threading.Thread(target=run_thread, args=(4,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



