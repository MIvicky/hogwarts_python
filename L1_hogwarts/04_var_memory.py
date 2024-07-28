# 以下三个变量是同一个变量，因为它们的内存地址相同
# 使用内置函数 id() 可以获取变量的内存地址
# 每个变量在内存中都有一个唯一的地址

print(id("Mary"))
# 4335835856
name = "Mary"
print(id(name))
# 4335835856
student = "Mary"
print(id(student))
# 4335835856