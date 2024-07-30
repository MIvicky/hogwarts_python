#【练习】回文数(循环实现)

# 知识点
# 类型转换
# 运算符
# 循环语句-for-in

# 作业要求
# 编写一个Python程序，输入一个5位数，判断输入的这个数字是否为回文数。
# 回文数是指从左到右和从右到左读都一样的数。例如12321。
# 如果输入的是回文数，输出是回文数，否则输出不是回文数。（使用循环进行实现）

# 之前用切片实现过
num1 = input("请输入一个五位数：")
if num1 == num1[::-1]:
    print(f"{num1}是回文数!")
else:
    print(f"{num1}不是回文数！")

# 循环实现
num2 = input("请输入一个数字：")
for i in range(len(num2) // 2):
    if num2[i] != num2[len(num2)-1-i]:
        print(f"{num2}不是回文数！")
        break
else:
    print(f"{num2}是回文数！")