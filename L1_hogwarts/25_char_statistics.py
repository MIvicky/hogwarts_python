#【练习】字符统计

# 知识点
# 分支语句
# 循环语句
# 字典

# 作业要求
# 从键盘输入一个字符序列，统计：大写字母，小写字母，数字，其它字符各出现次数，将次数保存到字典中。

str = input("请输入一个字符串：")

# 把字符串转换成列表，每一个字符为一个元素
str_list = list(str)

# 判断每个字符的类型
# isalpha() 如果 string 至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
# isdigit() 如果 string 只包含数字则返回 True 否则返回 False
# isalnum() 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# isupper() 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# islower() 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

# 设置字典记录字符出现的次数
char_count = {}

for char in str_list:
    if char.isupper():
        char_count["uppercase"] = char_count.get("uppercase", 0) + 1
    elif char.islower():
        char_count["lowercase"] = char_count.get("lowercase", 0) + 1
    elif char.isdigit():
        char_count["digit"] = char_count.get("digit", 0) + 1
    else:
        char_count["others"] = char_count.get("others", 0) + 1

for name, value in char_count.items():
    print(f"{name}的出现次数为：{value}")