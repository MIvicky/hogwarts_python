#【练习】固定数值计算

# 知识点
# 分支语句
# 循环语句
# 字典

# 作业要求
# 对数字列表中数字的求和，求平均值，求最大值，求最小值

list1 = [12,34,3,6,56,33434,6,3,23,23,23,57,78,11,1,8,9]

sum_result = 0
min_result = list1[0]
max_result = list1[0]

for n in list1:
    sum_result += n
    if n < min_result:
        min_result = n
    if n > max_result:
        max_result = n

avg_result = sum_result / len(list1)

print(f"列表求和：{sum_result}, 平均值：{avg_result}, 最大值：{max_result}, 最小值：{min_result}")