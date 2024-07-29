#【练习】字符串综合实战
# 作业要求：编写一个Python程序，对一个简单的故事进行如下操作：
# 统计故事中的单词数量。
# 查找主人公的名字在故事中的位置。
# 将主人公的名字替换为你的名字。
# 将故事改写为大写和小写形式。

story = "Once upon a time, in a land far away, lived a brave knight named Arthur."

# 统计故事中的单词数量
words_in_story = len(story.split(" "))
# 优化：story.split(" ") split参数空格可以省略，因为split默认就是使用空格作为分隔符
print(f"单词数量是：{words_in_story}")

# 查找主人公的名字在故事中的位置
user_index = story.find("Arthur")
print(f"主人公的名字在故事中的位置是：{user_index}")

# 将主人公的名字替换为你的名字
new_story = story.replace("Arthur", "Xinlan")
print(new_story)

# 将故事改写为大写和小写形式
print("大写形式：" + story.upper())
print("小写形式：" + story.lower())





