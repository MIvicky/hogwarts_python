# 【练习】猜数字

# 知识点
# 随机数生成-random 模块
# 循环语句-while
# 循环语句-for-in
# 用户输入-input()
# 变量操作-统计玩家猜测的总次数

# 作业要求
# 编写一个 Python 程序，实现一个猜数字的游戏。
# 程序随机生成一个1-100目标数字，在一定的范围内，玩家需要根据提示猜测目标数字，直到猜中为止。
# 游戏会根据玩家的猜测给出提示，告诉玩家猜的数字是大了还是小了，最终告诉玩家猜对了，并显示猜测次数。

from random import randint

right_num = randint(1, 100)
guess_count = 0

while True:
    user_num = int(input("请输入您猜测的数字："))
    guess_count += 1
    if user_num == right_num:
        print(f"恭喜！电脑生成的数字为：{right_num}，您猜对了！您一共猜测了 {guess_count} 次")
        break
    elif user_num < right_num:
        print("您猜测的数字小了！")
    else:
        print("您猜测的数字大了！")