#【练习】读写文件

# 知识点
# 文件操作

# 作业要求
# 编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来。

data = ["Hello,\n", "Python!\n", "Hi,\n", "Pytest!\n", "I love myself!\n"]
# 写入文件
file1 = open("test.txt", "w")
file1.writelines(data)
file1.close()

# 读取文件
file3 = open("test.txt", "r")
# 读取文件所有内容
print(file3.read())
file3.close()
# Hello,
# Python!
# Hi,
# Pytest!
# I love myself!

# 读取文件
file2 = open("test.txt", "r")
# 每read一次，文件指针就会移动到相应的位置
# 读取文件指针所在行剩余所有内容
print(file2.readline()) # Hello,
# 读取文件指针所在位置的前2个字符
print(file2.read(2)) # Py
# 读取文件指针所在行剩余所有内容
print(file2.readline()) # thon!
# 读取文件指针所在位置的前1个字符
print(file2.read(1)) # H
# 读取文件指针后所有内容，并以列表形式返回结果，一行内容为一个元素
print(file2.readlines()) # ['i,\n', 'Pytest!\n', 'I love myself!\n']
# 由于此时文件指针已经移动到文件末尾，后续没有内容，所以再读取文件内容就会为空
print(file2.read()) # 空内容
file2.close()
