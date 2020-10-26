# -*- coding: utf-8 -*-
# @Time     : 2020/10/26 20:07
# @Author   : liang
# @File     : class.py

class Computer():
    # 定义静态变量 即 类变量
    size = 15
    color = 'blue'
    momory = 258

    # 定义构造函数
    def __init__(self):
        # 定义实例变量
        self.cup = 'core i7'
        # 调用类变量
        print(self.color)
    def brand(self, name):
        self.name = name
        # 传参判断
        if self.name == 'lenovo':
            print("适用于商务公办")
        elif self.name == 'HuaWei':
            print("适用于高清拍照")
        elif self.name == 'Vivo':
            print("适用于音乐")

class Room():
    # 定义类变量
    door = 'black'
    size = 30

    # 定义方法
    def bedroom(self):
        bed = '双人床'
        self.desk = '多功能书桌'
        print(f"在{bed}上睡得舒服")

    def cook(self):
        print("在厨房可以做饭")
        print(self.desk)

class Play():

    def ball(self, ball):
        self.ball = ball
        # 判断传参
        if self.ball == 'basketball':
            print("记得叫我一起去")
        else:
            print(" Pass ")
    def rest(self, time_num):
        print(f"运动一次，休息{time_num}天")

class Work():
    work_type = 'IT'

    def  traffic_tools(self, weather):
        self.weather = weather
        if self.weather == 'sunny':
            print("坐公交去上班")
        elif self.weather == 'rainy':
            print("坐地铁去上班")
        elif self.weather == 'typhoon':
            print("不出门，哈哈")

class Reading():

    def book_type(self, type):
        self.type = type

        if self.type == 'testing':
            print("主要是工作的提升")
        elif self.type == 'history':
            print("了解中国历史文化")
        else:
            print("pass")

# c = Computer()
# c.brand('lenovo')
# w = Work()
# w.traffic_tools('sunny')




















