#【练习】模拟乘车过程

# 知识点
# 分支语句-if

# 作业要求
# 编写一个 Python 程序，模拟乘坐公交车过程，并且可以有座位坐下。
# 要求：输入公交卡当前的余额，只要不低于2元，就可以上公交车；如果车上有空座位，就可以坐下。

bus_card_balance = float(input("请输入您的公交卡余额："))

if bus_card_balance >= 2:
    print("余额足够，您可以乘坐公交！")
    isSeat = input("车上是否有空座位(有 / 没有)：")
    if isSeat == "有":
        print("您可以找空座位坐下！")
    else:
        print("没有空座位了！")
else:
    print("抱歉！您的余额不足2元，无法乘坐公交！")
