# 比如，在学习列表时的 sort() 排序方法，如果是简单的基本数据类型的数据，可以直接进行排序，
# 但如果是复杂结构的数据，需要根据自定义的规则进行排序，此时就可以使用 lambda

# 待排序的数据
students = [
    {'name': 'Alice', 'id': '1001', 'class': 'Class1'},
    {'name': 'Eve', 'id': '1005', 'class': 'Class2'},
    {'name': 'Charlie', 'id': '1003', 'class': 'Class1'},
    {'name': 'David', 'id': '1004', 'class': 'Class2'},
    {'name': 'Bob', 'id': '1002', 'class': 'Class1'},
    {'name': 'Frank', 'id': '1006', 'class': 'Class2'}
]

# 对于复杂结构的数据，直接使用sort()，而不传递排序规则，会报错
# students.sort()
# TypeError: '<' not supported between instances of 'dict' and 'dict'

# 使用 lambda 表达式传递排序规则
# 以名字排序
students.sort(key = lambda stu: stu["name"])
print(students)
# [{'name': 'Alice', 'id': '1001', 'class': 'Class1'}, {'name': 'Bob', 'id': '1002', 'class': 'Class1'}, {'name': 'Charlie', 'id': '1003', 'class': 'Class1'}, {'name': 'David', 'id': '1004', 'class': 'Class2'}, {'name': 'Eve', 'id': '1005', 'class': 'Class2'}, {'name': 'Frank', 'id': '1006', 'class': 'Class2'}]

# 以 id 降序排序
students.sort(key = lambda stu: stu["id"], reverse=True)
print(students)
# [{'name': 'Frank', 'id': '1006', 'class': 'Class2'}, {'name': 'Eve', 'id': '1005', 'class': 'Class2'}, {'name': 'David', 'id': '1004', 'class': 'Class2'}, {'name': 'Charlie', 'id': '1003', 'class': 'Class1'}, {'name': 'Bob', 'id': '1002', 'class': 'Class1'}, {'name': 'Alice', 'id': '1001', 'class': 'Class1'}]