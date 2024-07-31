# Sorted 函数实现原理

students = [
    {'name': 'Alice', 'id': '1001', 'class': 'Class1'},
    {'name': 'Eve', 'id': '1005', 'class': 'Class2'},
    {'name': 'Charlie', 'id': '1003', 'class': 'Class1'},
    {'name': 'David', 'id': '1004', 'class': 'Class2'},
    {'name': 'Bob', 'id': '1002', 'class': 'Class1'},
    {'name': 'Frank', 'id': '1006', 'class': 'Class2'}
]

def my_sorted(obj, key=None, reverse=False):
    new_students = []
    for student in students:
        for new_stu in new_students:
            # 存在排序规则
            if key:
                if key(student) < key(new_stu):
                    idx = new_students.index(new_stu)
                    new_students.insert(idx, student)
                    break
            # 不存在排序规则
            else:
                if student < new_stu:
                    idx = new_students.index(new_stu)
                    new_students.insert(idx, student)
                    break
        else:
            new_students.append(student)

    # 如果reverse为True,则倒序输出
    return new_students[::-1] if reverse else new_students

# 以 id 降序排序
students = my_sorted(students, key=lambda s: s["id"], reverse=True)
print(students)
# 以 name 升序排序
# students.sort(key=lambda s: s["name"])
# print(students)

students = [1,4,2,6,7,8,4,3,3]
students = my_sorted(students, reverse=True)
print(students)
# [8, 7, 6, 4, 4, 3, 3, 2, 1]
