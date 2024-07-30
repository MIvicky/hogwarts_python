#【练习】水仙花数

# 知识点
# 运算符
# 循环语句-for-in
# 分支语句-if
# 函数返回值与参数处理

# 作业要求
# 编写一个 Python 程序，找出100-999范围内的水仙花数。
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# 设置一个数组存放水仙花数
daffodil = []

# 初始版本
# for num in range(100, 1000):
#     # 百位
#     hundreds = num // 100
#     # 十位
#     tens = num % 100 // 10
#     # 个位
#     # individuals = num % 100 % 10
#     # 优化:
#     individuals = num % 10
#
#     if num == (hundreds**3 + tens**3 + individuals**3):
#         daffodil.append(num)

# 优化版本
for num in range(100, 1000):
    # 将数字转换成字符串，拆出百位、十位、个位
    # str_num = str(num)
    # hundreds = int(str_num[0])
    # 或者用一个数组存放百位、十位、个位
    digit = [int(n) for n in str(num)]
    # 计算百位、十位、个位的三次方之和
    sum_result = sum(n**3 for n in digit)

    # 判断是否是水仙花数
    if num == sum_result:
        daffodil.append(num)

print(f"100~999范围内的水仙花数有：{daffodil}")
# 100~999范围内的水仙花数有：[153, 370, 371, 407]