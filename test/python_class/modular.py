# -*- coding: utf-8 -*-
# @Time     : 2020/10/26 21:26
# @Author   : liang
# @File     : modular.py
from test.python_class.TongLao import TongLao

# 调用其他模块的类对象（模块化改造）
class WuYa(TongLao):

    def __init__(self,hp):
        self.hp = hp
        self.power = 200
        self.defense = 100
        # 通过继承调用父类的构造函数，拿到父类的属性
        # super().__init__(hp)

    def fight(self, enemy_hp):
        self.enemy_hp = enemy_hp
        self.enemy_pwoer = 200
        # 加入循环
        while True:
            # 回合制规则
            self.hp = self.hp +self.defense - self.enemy_pwoer
            self.enemy_hp = self.enemy_hp - self.power
            # 打印回合制的结果
            print(self.hp)

            # 回合制判断谁赢了
            if self.hp <= 0:
                print("敌人赢了")
                break
            elif self.enemy_hp <= 0:
                print("虚竹赢了")
                break
A = WuYa(1000)
A.fight(980)
A.see_people("a")
# if __name__ == '__main__':
#     A = XuZhu(200, 20)
#     A.fight(100, 10)

