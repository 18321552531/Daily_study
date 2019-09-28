# -*- coding: utf-8 -*-
# @Time    : 2019-09-28  13:59
# @File    : schedule_01.py
# @Author  : 啊啊

import schedule
import time
from datetime import datetime

def job(name):
    now = datetime.now().strftime('%Y%m%d-%H:%M:%S')
    print(f'do {name} job' + now)


now = datetime.now().strftime('%Y%m%d-%H:%M:%S')
with open('test.txt','a+') as f:
    f.write(now+'\n')
print('begin')
schedule.every().day.at('02:12').do(job,'run_ods_today')

while True:
    schedule.run_pending()
    time.sleep(1)




