#【练习】计算器

# 知识点
# 异常处理
# 分支语句-if
# 函数返回值与参数处理

# 作业要求
# 编写一个Python程序，可以执行加法、减法、乘法和除法操作。
# 用户可以输入两个数字和一个运算符，然后计算并输出结果。
# 实现计算器的功能（+、-、*、/），并处理异常情况，比如：输入的不是数字、除数为0等。

# float(input("请输入一个数字: "))
# ValueError: could not convert string to float: 'rr'
# 4 / 0
# ZeroDivisionError: division by zero

try:
    num1 = float(input("请输入第一个数字: "))
    num2 = float(input("请输入第二个数字: "))
    operator = input("请输入运算符（+、-、*、/）中的一个: ")

    if operator not in "+-*/" or len(operator) != 1:
        raise ValueError("输入的运算符不符合规范或超出范围")
    elif operator == "+":
        print(f"{num1} {operator} {num2} = {num1 + num2}")
    elif operator == "-":
        print(f"{num1} {operator} {num2} = {num1 - num2}")
    elif operator == "*":
        print(f"{num1} {operator} {num2} = {num1 * num2}")
    elif operator == "/":
        print(f"{num1} {operator} {num2} = {num1 / num2}")
except ValueError as ve:
    print("输入的数据有问题: ", ve)
except ZeroDivisionError as zero_err:
    print("除数不能为0: ", zero_err)
except Exception as err:
    print("其他问题: ", err)
finally:
    print("计算结束！")