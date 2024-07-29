# 字典操作
stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
print(stu.keys())
# dict_keys(['name', 'age', 'gender', 'address'])
print(stu.values())
# dict_values(['Tom', 23, 'male', 'BeiJing'])
print(stu.items())
# dict_items([('name', 'Tom'), ('age', 23), ('gender', 'male'), ('address', 'BeiJing')])

print(stu["name"]) # Tom
# print(stu["hobby"])
# 通过这种方式获取value，如果key不存在，则会报错 KeyError: 'hobby'

print(stu.get("name")) # Tom
print(stu.get("hobby")) # None
print(stu.get("hobby", "无数据")) # 无数据
# 通过 get(key, default) 方式获取value，如果key不存在，则返回设置的值，默认为None


# setdefault(key,default) 给一个不存在的 key 添加一个默认值并将该键值对保存到字典中。
stu.setdefault("hobby1")
print(stu)
# {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing', 'hobby1': None}
stu.setdefault("hobby2", "无")
print(stu)
# {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing', 'hobby1': None, 'hobby2': '无'}

# fromkeys(keys,val) 用于创建一个新字典，以序列 keys 中元素做字典的键，value 为字典所有键对应的初始值,默认为 None。
# 该方法是一个静态方法，需要使用字典类型名 dict 调用。
# 该方法如果给给定 keys 参数，则所有的key对应值都为默认值 None,
# 如果给定 val 值，则所有 key 对应的值为 val。
ks = ("name", "age", "gender")
s1 = dict.fromkeys(ks)
print(s1)
# {'name': None, 'age': None, 'gender': None}

s2 = dict.fromkeys(ks,"无")
print(s2)
# {'name': '无', 'age': '无', 'gender': '无'}

# update(dict | iterable) 使用参数中的数据更新当前字典。
# 该方法的参数可以接收一部字典（大多数的使用方式），也可以接收一个可迭代对象，
# 如果参数数据中的 key 在当前字典中存在，则使用新值更新字典中的键值对，
# 如果参数数据中的 key 在当前字典中不存在，则将键值对添加到当前字典中。

# 更新目标数据是一个字典
stu1 = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
newStu1 = {"name":"Jack","hobby":"eat"}
stu1.update(newStu1)
print(stu1)
# {'name': 'Jack', 'age': 23, 'gender': 'male', 'address': 'BeiJing', 'hobby': 'eat'}

# 更新目标数据是一个可迭代对象
stu2 = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
newStu2 = (("name","Rose"),["hobby","play"])
stu2.update(newStu2)
print(stu2)
# {'name': 'Rose', 'age': 23, 'gender': 'male', 'address': 'BeiJing', 'hobby': 'play'}

# popitem() 用来获取并删除字典中的最后一个键值对，返回一个元组
# 如果字典为空时，则抛出一个错误
stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
v = stu.popitem()
print(v) # ('address', 'BeiJing')
print(stu) # {'name': 'Tom', 'age': 23, 'gender': 'male'}

v = stu.popitem()
print(v) # ('gender', 'male')
print(stu) # {'name': 'Tom', 'age': 23}

# print({}.popitem())
# KeyError: 'popitem(): dictionary is empty'

# pop(key) 用于获取并删除字典中指定 key 对应的键值对。
# 如果指定的 key 不存在，则抛出错误
stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
v = stu.pop("name")
print(v) # Tome
print(stu)  # {'age': 23, 'gender': 'male', 'address': 'BeiJing'}
# v = stu.pop("score")
# KeyError: 'score'

# clear() 清空字典中所有的键值对元素
stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
print(stu)

stu.clear()
print(stu) # {}

print("====================")
# 集合
# update(others) 更新集合，添加来自 others 中的所有元素
# others 是一个可迭代对象，如果数据在集合中存在则不更新。
s = {1, 2, 3}

s.update((4,5,6))
print(s) # {1, 2, 3, 4, 5, 6}
s.update([5,6,7])
print(s) # {1, 2, 3, 4, 5, 6, 7}
s.update({6,7,8,9})
print(s) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# pop() 从集合中移除并返回任意一个元素，如果集合为空，则抛出错误
s = {7, 12, 4, 9}

print(s.pop()) # 9
print(s) # {12, 4, 7}
print(s.pop()) # 12
print(s) # {4, 7}
print(s.pop()) # 4
print(s) # {7}
print(s.pop()) # 7
print(s) # set()
# print(s.pop()) 空集合
# KeyError: 'pop from an empty set'

# remove(elem) 从集合中移除元素 elem。 如果 elem 不存在于集合中则抛出错误。
s = {1, 2, 3}

print(s.remove(1)) # None
print(s) # {2, 3}
print(s.remove(3)) # None
print(s) # {2}
# print(s.remove(5)) 如果 elem 不存在于集合中则抛出错误。
# KeyError: 5

# discard(elem) 如果元素 elem 存在于集合中则将其移除，如果 elem 不存在，则什么也不做
s = {1, 2, 3}

print(s.discard(1)) # None
print(s) # {2, 3}
s.discard(3)
print(s) # {2}
s.discard(5) # 如果 elem 不存在，则什么也不做

# clear() 清空集合
s = {1, 2, 3}
s.clear()
print(s) # set()

# 并集
# union(*other) 返回一个新集合，其中包含来自原集合以及 others 指定的所有集合中的元素
# other 可以指定多个集合。
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {5, 6, 7, 8}
print(s1.union(s2))
print(s1.union(s2,s3))
# 也可以使用 | 进行集合并集运算
print(s1 | s2)
print(s1 | s2 | s3)

# 交集
# intersection(*others) 返回一个新集合，其中包含原集合以及 others 指定的所有集合中共有的元素。
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {5, 6, 7, 8}
print(s1.intersection(s2)) # {3, 4}
print(s1.intersection(s2, s3)) # set()
print(s1.intersection(s3))
# 也可以使用 & 进行集合交集运算
print(s1 & s2)
print(s1 & s2 & s3)
print(s1 & s3)

# 差集
# difference(*others) 返回一个新集合，包含原集合中在 others 指定的其他集合中不存在的元素。
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {5, 6, 7, 8}
print(s1.difference(s2)) # {1, 2}
print(s1.difference(s2, s3)) # {1, 2}
print(s1.difference(s3)) # {1, 2, 3, 4}
# 也可以使用 - 进行集合差集运算
print(s1 - s2)
print(s1 - s2 - s3)
print(s1 - s3)

print("********************")
# 对称差集
# symmetric_difference(other) 返回一个新集合，其中的元素或属于原集合或属于 other 指定的其他集合，但不能同时属于两者。
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {5, 6, 7, 8}
print(s1.symmetric_difference(s2)) # {1, 2, 5, 6}
print(s1.symmetric_difference(s3)) # {1, 2, 3, 4, 5, 6, 7, 8}
# 也可以使用 ^ 进行集合对称差集运算
print(s1 ^ s2)
print(s1 ^ s3)
