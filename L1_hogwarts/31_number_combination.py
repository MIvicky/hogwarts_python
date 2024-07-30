#【练习】数字组合

# 知识点
# 分支语句-if
# 循环语句-for-in
# 循环嵌套

# 作业要求
# 编写一个 Python 程序，输出所有由数字1、2、3、4 组成的互不相同且无重复数字的三位数。
# 即个位，十位，百位互不相同且无重复数字。

num = [1, 2, 3, 4]

three_digit_number = []

for i in range(len(num)):
    for j in range(len(num)):
        for k in range(len(num)):
            # 如果当前选择的三位数字均不同的话，则合格
            if num[i] != num[j] and num[i] != num[k] and num[j] != num[k]:
                n = int(str(num[i]) + str(num[j]) + str(num[k]))
                three_digit_number.append(n)

print("所有由数字1、2、3、4 组成的互不相同且无重复数字的三位数: ")
print(three_digit_number)
