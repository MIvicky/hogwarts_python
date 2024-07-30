#【练习】冒泡排序

# 知识点
# 参数说明
# 条件语句 if-else
# 循环嵌套
# 列表操作
# 判断

# 作业要求
# 编写一个Python程序，实现冒泡排序。

# 默认为升序
def bubble_sort(num: list, reverse=False) -> list:
    for i in range(len(num)-1):
        for j in range(len(num)-i-1):
            if num[j] > num[j+1]:
                num[j+1], num[j] = num[j], num[j+1]

    # 如果reverse为True则倒序输出数组
    if reverse:
        return num[::-1]
    else:
        return num

list1 = [9, 5, 13, 4, 6, 9, 5, 20, 1]
print(bubble_sort(list1))
print(bubble_sort(list1, reverse=True))