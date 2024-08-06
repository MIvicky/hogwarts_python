#【练习】异常处理练习

# 知识点
# 异常处理

# 作业要求
# 编写程序，让用户输入两个整数start和end,然后输出这两个整数之间的一个随机数。
# 要求考虑用户输入不是整数的情况，以及start>end的情况。根据实际情况进行适当提示或输出。

from random import randint

# int(input("请输入一个整数: "))
# ValueError: invalid literal for int() with base 10: 'er'
# randint(5, 3)
# ValueError: empty range in randrange(5, 4)

try:
    start = int(input("请输入一个整数start: "))
    end = int(input("请输入一个整数end: "))

    if start > end:
        # 手动抛出异常
        raise ValueError("起始值start不能大于结束值end")
except ValueError as ve:
    print("输入的数据有问题：", ve)
except Exception as err:
    print("其他问题：", err)
else:
    print(f"{start} 和 {end} 之间的一个随机整数为：{randint(start, end)}")
finally:
    print("结束！")

