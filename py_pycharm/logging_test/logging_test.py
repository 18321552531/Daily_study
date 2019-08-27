# -*- coding: utf-8 -*-
# @Time    : 2019-08-27  22:12
# @File    : logging_test.py
# @Author  : 啊啊

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='/Users/zhushengzu/python_load/py_pycharm/log_file/log_test.txt',
    filemode='a',
    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    )

hello = 'hello_world'
logging.debug(hello)

print(hello)


