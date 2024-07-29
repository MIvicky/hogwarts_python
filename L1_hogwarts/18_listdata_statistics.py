#【练习】数据统计

# 知识点
# 列表
# 变量
# 循环语句

# 作业要求
# 列表中保存若干个数字，计算数字的和，最小值，最大值，平均数

list1 = [23456, 234, 23, 423, 423, 423, 423, 412, 3235, 346, 47, 5687, 678, 7, 453623, 4523, 565, 786, 9789, 567,
            34634, 234]

i = 1
# 数字的和
sum_result = list1[0]
# 最小值
min_result = list1[0]
# 最大值
max_result = list1[0]

while i < len(list1):
    sum_result += list1[i]
    if list1[i] < min_result:
        min_result = list1[i]
    if list1[i] > max_result:
        max_result = list1[i]
    i += 1

# 平均值
avg_result = sum_result / len(list1)

print(f"list1: {list1}")
print(f"列表list1中数字的和为: {sum_result}, 最大值为：{max_result}, 最小值为: {min_result}, 平均值为：{avg_result}")
