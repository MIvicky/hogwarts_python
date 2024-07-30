# 【练习】打印图案

# 知识点
# 循环语句-for-in
# 循环嵌套

# 作业要求:
# 编写一个Python程序，分别打印以下图案。
# 图案1正方形如下：
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
for _ in range(5):
    for _ in range(5):
        print("*", end="  ")
    print("")

print("=" * 20)
# 图案2直角三角形如下：
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
for i in range(5):
    for j in range(i+1):
        print("*", end="  ")
    print("")

print("=" * 20)
# 图案3倒立直角三角形如下：
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
for i in range(5):
    for j in range(i, 5):
        print("*", end="  ")
    print("")

print("=" * 20)
# 图案4等腰三角形如下：
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
for i in range(5):
    # 打印每一行的空格
    for j in range(5-(i+1)):
        print(" ", end="  ")
    # 打印空格后的"*"图案
    for j in range(2*(i+1)-1):
        print("*", end="  ")
    print("")

print("=" * 20)
# 打印倒着的等腰三角性能
for i in range(5):
    # 打印每一行的空格
    for j in range(i):
        print(" ", end="  ")
    # 打印空格后的"*"图案
    for j in range(2*(5-i)-1):
        print("*", end="  ")
    print("")