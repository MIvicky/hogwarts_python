#【练习】猜拳游戏

# 知识点
# 随机数生成-Python 的内置模块 random
# 分支语句-if-elif-else
# 输入-input()

# 作业要求
# 编写一个Python程序，实现一个简单的猜拳游戏。
# 玩家和电脑各自选择石头、剪刀或布，根据规则判断胜负关系，并输出比赛结果。
import random

game_cards = ["石头", "剪刀", "布"]

player_choose = input("请输入你的选择，石头、剪刀或者布：")
computer_choose = random.choice(game_cards)
print("电脑的选择是：" + computer_choose)

# 玩家和电脑出的选择一致
if player_choose == computer_choose:
    print("平局！")
elif player_choose == "石头":
    # 玩家出石头，电脑出剪刀
    if computer_choose == "剪刀":
        print("玩家赢！")
    # 玩家出石头，电脑出布
    else:
        print("电脑赢！")
elif player_choose == "剪刀":
    # 玩家出剪刀，电脑出石头
    if computer_choose == "石头":
        print("电脑赢！")
    # 玩家出剪刀，电脑出布
    else:
        print("玩家赢！")
else:
    # 玩家出布，电脑出石头
    if computer_choose == "石头":
        print("玩家赢！")
    # 玩家出布，电脑出剪刀
    else:
        print("电脑赢！")
