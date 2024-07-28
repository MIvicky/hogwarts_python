# 使用 type() 查看变量的具体类型
print(type(666))
# <class 'int'>
print(type(23.1))
# <class 'float'>
print(type(23.56))
# <class 'float'>
# Python3中没有 double 双精度浮点型
print(type(1+2j))
# <class 'complex'>
# 复数包含实部和虚部，虚部由 j 或 J 表示，示例：1+2j, -1.5+3.5j
print(type(True))
# <class 'bool'>
print(type("aaa"))
# <class 'str'>
print(type((1,2,3)))
# <class 'tuple'>
print(type([1,2,3]))
# <class 'list'>
print(type({1,2,3}))
# <class 'set'>
print(type({"name":"xinlan", "age":13}))
# <class 'dict'>
print(type(None))
# <class 'NoneType'>

# 类型转换
# 自动转换（隐式类型转换）
n = 10 + 3.14
print(n, type(n))
# 13.14 <class 'float'>

n = False + 1
print(n, type(n))
# 1 <class 'int'>

# 强制转换（显示类型转换）
# title = "霍格沃兹" + 666
# print(title, type(title))
# TypeError: can only concatenate str (not "int") to str

title = "霍格沃兹" + str(666)
print(title, type(title))
# 霍格沃兹666 <class 'str'>

# x1 = int("hogwarts")
# ValueError: invalid literal for int() with base 10: 'hogwarts'

# 将字符串转换为整数
x = int("123")
print(x, type(x))
# 123 <class 'int'>

# 将字符串转换为浮点数
y = float("3.14")
print(y, type(y))
# 3.14 <class 'float'>

# 将数字转换为字符串
z = str(123)
print(z, type(z))
# 123 <class 'str'>

# 将数字转换为布尔类型
b = bool(123)
print(b, type(b))
# True <class 'bool'>

# 将数字转换为字符
c = chr(65)
print(c, type(c))
# A <class 'str'>

print("=======================")

# 示例 1
str1 = "Hello"
str2 = "Hello"
print(id(str1))  # 输出第一个字符串对象的内存地址 4334931808
print(id(str2))  # 输出第二个字符串对象的内存地址 4334931808
print(str1 == str2) # True 字面量相同
print(str1 is str2) # True 内存地址相同

# 示例 2
str3 = "Hello, World!" * 1000
str4 = "Hello, World!" * 1000
print(id(str3))  # 输出第一个字符串对象的内存地址 5612212736
print(id(str4))  # 输出第二个字符串对象的内存地址 5612226048
print(str3 == str4) # True 字面量是相同的
print(str3 is str4) # False 内存地址不同

print("=======================")

# 示例 1
str3 = "Hello"
str4 = "Hello"
print(id(str3))  # 输出第一个字符串对象的内存地址 4334931808
print(id(str4))  # 输出第二个字符串对象的内存地址 4334931808
print(str3 == str4) # True 字面量相同
print(str3 is not str4) # False 内存地址相同

# 示例 2
str5 = "Hello, World!" * 1000
str6 = "Hello, World!" * 1000
print(id(str5))  # 输出第一个字符串对象的内存地址 5612226048
print(id(str6))  # 输出第二个字符串对象的内存地址 5612212736
print(str5 == str6) # True 字面量是相同的
print(str5 is not str6) # True 内存地址不同

print(0 == False) # True
print(2 == True) # False
print(2 == "2") # False

print("=======================")

a, b = 1, 1
# 判断a，b 是否相等
print(a == b) # True 值相同
print(a is b) # True 内存地址相同

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2) # True 值相同
print(list1 is list2) # False 内存地址不同