# -*- coding: utf-8 -*-
# @Time     :2020/10/21 21:23 
# @Author   :liang
# @File     :game_round.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

# 定义fight函数
def fight():
    # 定义4个变量，且赋值参数
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 192

# 加入循环，游戏多个回合制
    while True:
        # 游戏规则
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        print(my_hp)

        # 判断最后谁的血量小于等于0
        if my_hp <= 0:
            print("我输了")
            # 满足条件终止循环
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break
# 调用函数

fight()

