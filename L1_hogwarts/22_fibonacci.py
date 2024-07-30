# 【练习】斐波那契 for

# 知识点
# 列表操作
# 循环语句-for-in

# 作业要求
# 编写一个Python程序，使用for循环，生成并输出斐波那契数列的前n项，其中n是用户指定的正整数。
# 斐波那契数列，又称黄金分割数列，指的是：1、1、2、3、5、8、13、21、34....
# 从第三个数开始，每个数字都是前两个数字之和。

# f(n) = f(n-1) + f(n-2)

fibonacci = []

num = int(input("请输入n："))

for i in range(num):
    if i == 0 or i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)