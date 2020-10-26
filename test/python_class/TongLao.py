# -*- coding: utf-8 -*-
# @Time     : 2020/10/26 20:07
# @Author   : liang
# @File     : TongLao.py

class TongLao():
    #构造函数，定义实例变量
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
    #定义动态方法（即函数）
    def see_people(self, name):
        self.name = name
       # 判断传入参数，打印
        if self.name == "无崖子":
            print("师弟！！！！")
        elif self.name == "李秋水":
            print("师弟是我的！")
        elif self.name == "丁春秋":
            print("叛徒！我杀了你！")
        else:
            print("哈哈，我是跑龙套的！")
    def fight_zms(self, enemy_hp, enemy_power):
        self.enemy_hp = enemy_hp
        self.enemy_pwoer = enemy_power
        self.hp = self.hp/2
        self.power = self.power * 10

        # 回合制规则
        self.hp = self.hp - self.enemy_pwoer
        self.enemy_hp = self.enemy_hp - self.power
        #打印回合制的结果
        print(self.hp)
        print(self.enemy_hp)
        #回合制判断谁赢了
        if self.hp > self.enemy_hp:
            print("童姥赢了")
        else:
            print("敌人赢了")
 # 继承 Tonglao类（父类）
class XuZhu(TongLao):

    def read(self):
        print("罪过罪过")

if __name__ == '__main__':
    a = TongLao(1000, 200)
    a.see_people("无崖子")
    a.see_people("李秋水")
    a.see_people("丁春秋")
    a.fight_zms(1500, 300)
    b = XuZhu(100,20)
    b.read()