# 输出一个数据
print("Hello World")
# 输出多个数据
print("Hello", "Python", 20, True)
# 指定分隔符
print("Hello", "Python", 20, True, sep='---')
# 指定结束符
print("Hello", end="")
print("World")
print("Python", end="---")
print("Java")

print("aaa", 80, "bbb", False, sep="&", end="*******")
print("ccc", 100, "bbb", False, sep="+", end="------")
print("print函数")

# 【练习】打印专属用户欢迎信息
# 接受用户键盘输入，提示用户输入用户名，打印对应名户名的欢迎信息。
user_name = input("请输入您的用户名：")
print("欢迎用户：" + user_name + " 加入我们的大家庭！")