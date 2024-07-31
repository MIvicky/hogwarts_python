# 【练习】斐波那契数列

# 知识点
# 分支语句-if
# 递归算法
# 函数返回值与参数处理

# 作业要求
# 编写一个Python程序，使用递归算法，生成并输出斐波那契数列的第n项，其中n是用户指定的正整数。
# 斐波那契数列，又称黄金分割数列，指的是：1、1、2、3、5、8、13、21、34....从第三个数开始，每个数字都是前两个数字之和。

def fibonacci(n):
    if n < 1:
        return "输入错误"
    # 基本条件
    if n == 1 or n == 2:
        return 1
    # 减小问题规模
    return fibonacci(n-1) + fibonacci(n-2)

user_input = int(input("请输入正整数n: "))
print(f"斐波那契数列的第 {user_input} 项为：{fibonacci(user_input)}")
