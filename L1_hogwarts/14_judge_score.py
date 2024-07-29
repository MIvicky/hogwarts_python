#【练习】成绩判断

# 知识点
# 类型转换
# 分支语句-if

# 作业要求
# 编写一个 Python 程序，用户输入一个分数，程序将根据分数判断并输出相应的等级。
# 分数在 90 分及以上为 A 等级，60-89 分为 B 等级，否则为 C 等级。

student_score = int(input("请输入您的考试分数："))
# grade = "无等级"

if student_score >= 90:
    grade = "A"
# elif student_score >= 60 and student_score <= 89:
elif student_score >= 60:
    grade = "B"
else:
    grade = "C"

print(f"您的考试等级为: {grade}")