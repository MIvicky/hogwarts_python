#【练习】非固定数值计算

# 知识点
# 分支语句
# 循环语句

# 作业要求
# 输入任意数字求和，求平均值，求最大值，求最小值,直到输入bye结束，计算数字不考虑浮点数。

numbers = []
sum = 0
max = None
min = None
count = 0

while True:
    is_negative_num = False
    user_num = input("请输入整数(结束输入bye): ")

    if user_num == "bye":
        break

    # 如果输入的是负整数
    if user_num.startswith("-"):
        # 先去掉负号
        user_num = user_num[1:]
        is_negative_num = True

    if user_num.isdigit():
        user_num = int(user_num)
        if is_negative_num:
            user_num = user_num * -1

        # 记录输入的数字次数 和 数字
        count += 1
        numbers.append(user_num)

        # 求和
        sum += user_num

        # 最大值
        if max == None:
            max = user_num
        elif user_num > max:
            max = user_num

        # 最小值
        if min == None:
            min = user_num
        elif user_num < min:
            min = user_num

# 平均值：
avg1 = sum / count
avg2 = sum / len(numbers)

print(f"输入的数字为：{numbers}")
print(f"求和：{sum}, 平均值：{avg1}, 最大值：{max}, 最小值：{min}")
print(f"求和：{sum}, 平均值：{avg2}, 最大值：{max}, 最小值：{min}")
