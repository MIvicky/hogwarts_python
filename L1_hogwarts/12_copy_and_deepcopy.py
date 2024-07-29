# 浅拷贝
import copy

# 原始数据
origin_data = [[1, 2], {"name":"Tom", "chars":["A","B"]}]
print(id(origin_data)) # 4308699072

# 使用对象的copy()方法得到浅拷贝对象
copy_data1 = origin_data.copy()
# 拷贝成功的验证，内容相同，地址不同
print(copy_data1) # [[1, 2], {'name': 'Tom', 'chars': ['A', 'B']}]
print(id(copy_data1)) # 4309441088

# 使用工厂方法获取浅拷贝对象
copy_data2 = list(origin_data)
print(copy_data2) # [[1, 2], {'name': 'Tom', 'chars': ['A', 'B']}]
print(id(copy_data2)) # 4308699264

# 使用切片方式获取浅拷贝对象
copy_data3 = origin_data[:]
print(copy_data3) # [[1, 2], {'name': 'Tom', 'chars': ['A', 'B']}]
print(id(copy_data3)) # 4309441664

# 使用copy模块中的copy方法获取浅拷贝对象
copy_data4 = copy.copy(origin_data)
print(copy_data4) # [[1, 2], {'name': 'Tom', 'chars': ['A', 'B']}]
print(id(copy_data4)) # 4309382464

# 当修改任意浅拷贝对象时，其他的浅拷贝对象均会收到影响
copy_data3[1]["name"] = "Xinlan"
print(origin_data)
print(copy_data1)
print(copy_data2)
print(copy_data3)
print(copy_data4)
# 这些对象的值均被修改为了：# [[1, 2], {'name': 'Xinlan', 'chars': ['A', 'B']}]

print("=" * 20)

# 深拷贝
# import copy

# 原始数据
origin_data_deep = [[1,2],{"name":"Tom", "chars":["A","B"]}]

# 使用copy模块中的deepcopy方法获取深拷贝对象
deep_copy_data = copy.deepcopy(origin_data_deep)

# 拷贝成功的验证，内容相同，地址不同
# 查看所有对象内容
print(origin_data_deep) # [[1, 2], {'name': 'Tom', 'chars': ['A', 'B']}]
print(deep_copy_data) # [[1, 2], {'name': 'Tom', 'chars': ['A', 'B']}]
# 查看所有对象地址
print(id(origin_data_deep)) # 4343898048
print(id(deep_copy_data)) # 4343899648

# 当修改任意深拷贝对象时，其他的对象都不会受到影响
deep_copy_data[1]["chars"][0] = "CCC"
print(deep_copy_data)
# [[1, 2], {'name': 'Tom', 'chars': ['CCC', 'B']}]
print(origin_data_deep)
# [[1, 2], {'name': 'Tom', 'chars': ['A', 'B']}]
