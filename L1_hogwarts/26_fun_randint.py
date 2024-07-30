# 生成随机整数
from random import randint

# 语法: randint(start, stop) 包含start和stop
# 生成 1 ~ 3 之间的一个随机整数
print(randint(1, 3))

# 骰子游戏：从键盘输入一个数字，和程序随机生成的 1~6 范围的数字比较大小
user_num = int(input("请输入[1, 6]中间的一个整数: "))
computer_num = randint(1, 6)
print(f"电脑的数字是：{computer_num}")

if user_num > 6 or user_num < 1:
    print("您输入的是无效数字！")
elif user_num == computer_num:
    print("平局！")
elif user_num > computer_num:
    print("您赢了！")
else:
    print("电脑赢了！")