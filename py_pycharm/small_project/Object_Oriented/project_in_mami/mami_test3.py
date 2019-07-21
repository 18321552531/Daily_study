# -*- coding: utf-8 -*-
# @Time    : 2019-07-21  11:37
# @File    : mami_test3.py
# @Author  : 啊啊

'''
自定义用户信息数据结构， 写入文件, 然后读取出内容, 利用json模块进行数据的序列化和反序列化
定义用户类，定义方法db，例如 执行obj.db可以拿到用户数据结构
在该类中实现登录、退出方法, 登录成功将状态(status)修改为True, 退出将状态修改为False
(退出要判断是否处于登录状态).
密码输入错误三次将设置锁定时间(下次登录如果和当前时间比较大于30秒即不允许登录)
'''

'''
data={
    "egon":{"password":"123",‘status‘:False,‘timeout‘:0},
    "alex":{"password":"456",‘status‘:False,‘timeout‘:0},
}
'''
import json
import time

class User(object):
    # 用户类
    def __init__(self):
        self.user_dic = self.read()
        self.user_name = ''  #记录当前用户名字

    def write(self):
        with open('user_info', 'r', encoding='utf-8') as f:
            json.dump(self.user_dic, f)

    def read(self):
        """拿到用户数据"""
        with open('user_info', 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic

    def db(self):
        print('用户数据结构：', self.user_dic)

    def login(self):
        i = 0
        while i < 3:
            username = input('username:').strip()
            password = input('password:').strip()
            if username in self.user_dic and password == self.user_dic[username]["password"]:
                time_now = time.time()
                period = time_now - self.user_dic[username]["timeout"]  # 时间差
                if period >= 30:
                    print('%s登入成功' %(username))
                    self.username = username
                    self.user_dic[username]["status"] = True  # 记录用户登录状态
                    self.write()  # 将修改保存到文件
                    break
                else:
                    print("用户处于锁定状态，请%s S后再试" % (30 - period))
                    break
            else:
                print("用户名或密码错误！")
                i += 1
                if i == 3 and username in self.user_dic:
                    self.user_dic[username]["timeout"] = time.time()  # 记录3次登录失败的时间点
                    self.write()  # 将修改保存到文件
                    exit("退出")

    def exit(self):
        '退出'
        if self.username:  # 用户处于登录状态
            self.user_dic[self.username]["status"] = False  # 修改用户登录状态
            self.write()  # 将修改保存到文件
            exit("用户%s退出登录" % self.username)

    def help_info(self):
        print("""命令列表：
                 查看数据结构：db
                 登录：login
                 退出登录：exit""")

    def handle(self):
        """处理用户输入命令"""
        while True:
            cmd = input("请输入命令:").strip()
            cmd = cmd.split()
            if hasattr(self, cmd[0]):  # 使用反射
                func = getattr(self, cmd[0])  # 拿到方法名
                func()
            else:
                self.help_info()  # 打印帮助信息

user = User()
if __name__ == "__main__":
    user.handle()



