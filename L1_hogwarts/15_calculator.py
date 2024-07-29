#【练习】计算器

# 知识点
# 类型转换
# 运算符
# 分支语句-if

# 作业要求
# 编写一个简单的Python程序，实现一个简易的计算器。
# 用户可以输入两个数字以及一个运算符（+、-、*、/），程序将根据运算符执行相应的计算操作，并输出结果。

# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
operator = input("请输入一个运算符（+、-、*、/）：")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "抱歉！除数不能为0！"
    else:
        result = num1 / num2
else:
    result = "无效运算符！"

print(f"{num1} {operator} {num2} = {result}")