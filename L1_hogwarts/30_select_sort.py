#【练习】选择排序

# 知识点
# 列表操作
# 循环嵌套
# 判断
# 时间复杂度分析
# 变量
# 索引

# 作业要求
# 编写一个Python程序，实现选择排序。

def select_sort(num: list, reverse=False) -> list:
    # 选择排序-升序：选择当前未排序序列中最小的值放在已排序序列的最后
    for i in range(len(num)-1):
        min_index = i
        for j in range(i+1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
        # 将找出的最小值的索引放在已排序序列的最后
        num[i], num[min_index] = num[min_index], num[i]

    # 如果reverse=True，则倒序输出数组
    if reverse:
        return num[::-1]
    else:
        return num

list1 = [9, 5, 13, 4, 6, 9, 5, 20, 1]
print(select_sort(list1))
print(select_sort(list1, reverse=True))