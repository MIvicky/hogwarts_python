# 【练习】阶乘

# 知识点
# 分支语句-if
# 递归算法
# 函数返回值与参数处理

# 作业要求
# 编写一个Python程序，使用递归算法，计算给定正整数n的阶乘。
# 一个正整数的阶乘 factorial 是所有小于及等于该数的正整数的积，并且 0 的阶乘为 1。例如3的阶乘为1*2*3=6。

# 找到规律，减小问题规模
# f(0)=1, f(1)=1, f(2)=2*1=2*f(1), f(3)=3*2*1=3*f(2), f(4)=4*3*2*1=4*f(3)...
def factorial(n):
    if n < 0:
        return "参数错误"
    # 基本情况
    if n == 0 or n == 1:
        return 1
    # 减小问题规模
    return factorial(n-1) * n

user_input = int(input("请输入正整数n: "))
print(f"{user_input}的阶乘为：{factorial(user_input)}")