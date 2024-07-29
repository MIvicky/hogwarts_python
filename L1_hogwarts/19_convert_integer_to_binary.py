#【练习】整数转二进制数

# 知识点
# 循环语句
# 运算符

# 作业要求
# 编写一个 Python 程序，输入一个整数，计算该整数的二进制表示形式

num = int(input("请输入一个整数："))

result = ""
data = num

while data != 0:
    # 得到当前位置的二进制值
    tmp = data % 2
    # 得到剩余待转换的数值
    data //= 2
    # 注意：当前位置的二进制值一定要拼接在【最前面】
    result = str(tmp) + result

print(f"{num}转换成二进制的结果为：{result}")


