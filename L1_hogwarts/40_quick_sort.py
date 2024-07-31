# 【练习】快速排序

# 知识点
# 递归
# 分区操作
# 列表操作
# 算法复杂度分析

# 作业要求
# 编写一个Python程序，实现快速排序。

# 解题思路
# 首先选择一个基准元素，通常是选择待排序列表的第一个元素。
# 将列表分成两部分，小于基准元素的元素放在左边，大于基准元素的元素放在右边。这个过程称为分区（partition）。
# 递归地对左右两个分区进行快速排序。也就是将左边的分区作为新的子列表，再次选择基准元素，并进行分区操作。对右边的分区也是同样的操作。
# 递归的结束条件是分区中只有一个元素或为空，此时分区已经是有序的。
# 最后将所有的分区合并起来，即可得到排好序的列表。

def quick_sort(arr: list):
    # 基本情况
    if len(arr) <= 1:
        return arr

    # 选择数组中间的元素作为基准元素
    pivot = arr[len(arr) // 2]
    # 小于基准值的元素放在左边列表
    left = [x for x in arr if x < pivot]
    # 等于基准值的元素放在中间列表
    middle = [x for x in arr if x == pivot]
    # 大于基准值的元素放在右边列表
    right = [x for x in arr if x > pivot]

    # 对左右两边的列表继续进行排序
    # 合并结果返回
    return quick_sort(left) + middle + quick_sort(right)


list1 = [9, 5, 13, 4, 6, 9, 5, 20, 1]

# 升序
list2 = quick_sort(list1)
print(list2)
# [1, 4, 5, 5, 6, 9, 9, 13, 20]
# 倒序
# list2.reverse()
# print(list2)
# [20, 13, 9, 9, 6, 5, 5, 4, 1]
# 倒序
print(list2[::-1])
# [20, 13, 9, 9, 6, 5, 5, 4, 1]