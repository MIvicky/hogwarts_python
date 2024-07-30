# 【练习】素数

# 知识点
# 运算符
# 循环语句-for-in
# 分支语句-if
# 函数返回值与参数处理

# 作业要求
# 编写一个Python程序，输入一个正整数，判断这个数是否为素数（质数）。
# 素数是指只能被1和它本身整除的正整数。1和负数肯定不是素数。

import math

num = int(input("请输入一个正整数："))

def is_prime(num):
    num_is_prime = True
    if num <= 1:
        num_is_prime = False
    # 优化：不需要从[2,num)循环完所有的数，只需要循环到平方根就可以了
    # 对于大于1的数，从2开始到这个数的平方根（包括平方根），逐个检查是否能整除。
    # 如果存在能整除的数，则不是素数。
    for i in range(2, int(math.sqrt(num))+1):
    # for i in range(2, num):
        if num % i == 0:
            num_is_prime = False

    return num_is_prime

result = is_prime(num)
if result:
    print(f"{num}是素数！")
else:
    print(f"{num}不是素数！")