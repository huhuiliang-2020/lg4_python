# -*- coding: utf-8 -*-
# @Time     :2020/10/21 21:24 
# @Author   :liang
# @File     :game_random.py

import random

# 定义fight函数
def fight(enemy_hp, enemy_power):
    # 定义2个变量且赋值参数（储存数据）
    my_hp = 1000
    my_power = 200

    # 打印enemy_hp与enemy_power
    print(f"敌人的血量为{enemy_hp}, 敌人的攻击力为{enemy_power}")

# 加入循环，游戏多个回合制
    while True:
        # 游戏规则
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 判断双方最后谁的血量小于等于0
        if my_hp <=0:
            print(f"我的最后血量为{my_hp}")
            print(f"敌人的最后血量为{enemy_hp}")
            print("我输了")
            break
        elif enemy_hp <=0:
            print(f"我的最后血量为{my_hp}")
            print(f"敌人的最后血量为{enemy_hp}")
            print("我赢了")
            break

if __name__ == "__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(900, 1100)]
    # hp = []
    # for i in range(900, 1100):
    #     hp.append(i)
    # print(hp)

    # enemy_hp从hp列表中随机挑选一个值
    enemy_hp = random.choice(hp)

    #enemy_power用randint方法生成随机整数
    enemy_power = random.randint(190, 210)

# 调用函数fight，传入敌人的hp和power
    fight(enemy_hp, enemy_power)
