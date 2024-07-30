#【练习】词频统计

# 知识点
# 列表
# 列表操作
# 字符串操作
# 字典
# 字典操作
# for-in循环
# 分支语句-if

# 作业要求
# 编写一个Python程序，来计算给定文本中每个单词出现的次数。

text = """
Python is a popular programming language. It is widely used for web development, data science, and more.
Python has a simple and readable syntax, which makes it great for beginners.
"""

# # 将文本转换为小写并按照空格分割为单词
text_list = text.lower().split()
word_count = {}

for word in text_list:
    # 去掉单词中包含的标点符号
    # word = word.replace(".", "") if "." in word else word
    # word = word.replace(",", "") if "," in word else word
    # strip(chars): 删除string左右两侧的空白字符, 如果指定chars参数，则删除左右两侧指定的字符
    word = word.strip(".,!?")
    # 统计每个单词出现的次数
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")
