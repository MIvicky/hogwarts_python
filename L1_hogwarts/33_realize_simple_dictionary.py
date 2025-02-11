# 【练习】字典实现

# 知识点
# 字符串处理
# 字典
# 循环语句 for-in
# 分支语句 if-else

# 作业要求
# 编写一个Python程序，实现一个简单的字典。
# 将txt中的单词和翻译分别提取出来，构建一个字典。字典的键是英文单词，值是对应的中文翻译。

# 解题思路
# 文本数据初始化：字符串 txt 包含了英文单词和对应的中文翻译。
# 字符串分割：将字符串 txt 根据换行符和空格进行分割，得到一个包含多个字符串的列表。
# 构建字典：遍历字符串列表中的每个字符串，去掉可能的 # 标志，然后将单词和翻译分别提取出来，构建一个字典。字典的键是英文单词，值是对应的中文翻译。
# 用户输入和翻译查找：用户被提示输入一个英文单词。程序检查字典中是否存在该单词，如果存在则输出对应的中文翻译，否则提示单词不存在。

txt = '''#a
    Trans:art. 一;字母A
    #a.m.
    Trans:n. 上午
    #a/c
    Trans:n. 往来帐户@往来:come - and - go; contact; intercourse@n. 往来帐户
    #aardvark
    Trans:n. 土猪
    #aardwolf
    Trans:n. 土狼
    #aasvogel
    Trans:n. 秃鹰之一种
    #abaci
    Trans:n. 算盘
    #aback
    Trans:ad. 向后地;朝后地
    #abacus
    Trans:n. 算盘
    #abaft
    Trans:ad. 向船尾@prep. 在...后
    #abalone
    Trans:n. 鲍鱼
    #abandon
    Trans:vt. 放弃;沉溺@n. 放任
    #abandoned
    Trans:a. 被抛弃的;自弃的;自甘堕落的
    #abandonee
    Trans:n. 被遗弃者;被委付者
    #abandoner
    Trans:n. 遗弃者;委付者
    #abandonment
    Trans:n. 放弃;自暴自弃;放纵
    #abas
    Trans:vt. 打倒
    #abase
    Trans:vt. 降低...的地位;降低...的品格;贬抑
    #abasement
    Trans:n. 贬抑;屈辱;谦卑
    #abash
    Trans:vt. 使...羞愧;使困窘
    #abashment
    Trans:n. 羞愧;
    #abate
    Trans:vt. 缓和;减弱;减少;废除@vi. 缓和;减弱;减少
    #abatement
    Trans:n. 减少;减轻;缓和
    #abatis
    Trans:n. 鹿柴;拒木;铁丝网
    #abatment
    Trans:n. 消除，减除
    #abb
    Trans:n. 横丝;纬;羊毛
    #abbacy
    Trans:n. 大修道院院长之职位;管区;任期
    #abbatial
    Trans:a. 大修道院的;大修道院长的;女大修道院长的
    #abbe
    Trans:n. 大修道院院长;僧侣;神父
    #abbess
    Trans:n. 女修道院院长;女庵主持
    #abbey
    Trans:n. 修道院
    #abbot
    Trans:n. 修道院院长;方丈;住持
    #abbreviate
    Trans:vt. 缩写;使...简略;缩短
    #abbreviation
    Trans:n. 缩写
    #abbreviator
    Trans:n. 缩写者
    #abc
    Trans:n. 基础知识;美国广播公司;澳大利亚广播公司
    #abcoulomb
    Trans:n. 绝对库伦
    #abdicate
    Trans:vt. 放弃@vi. 逊位
    #abdication
    Trans:n. 逊位;弃权;辞职
    #abdicator
    Trans:n. 放弃者;让位者
    #abdomen
    Trans:n. 腹部
    #abdominal
    Trans:a. 腹部的;腹式呼吸;开腹手术
    #abduct
    Trans:vt. 诱拐;绑走
    #abduction
    Trans:n. 诱拐
    #abductor
    Trans:n. 诱拐者
    #abe
    Trans:n. 亚伯;Abraham 的昵称
    #abeam
    Trans:ad. 与船的龙骨成直角
    #abecedarian
    Trans:n. 初学者@a. 字母的;初步的
    #abed
    Trans:ad. 在床上
    #abelmosk
    Trans:n. 秋葵
    #aberrance
    Trans:n. 脱离正道;越轨;脱离常轨
    #aberrant
    Trans:a. 脱离正道的;脱离常轨的;变体的
    #aberration
    Trans:n. 越轨;光行差;心理失常;色差
    #abestrine
    Trans:adj. 石棉的
    #abet
    Trans:vt. 教唆;帮助'''

# 以一个单词一个翻译为一组拆分字符串
word_list = txt.split("\n    #")
print(word_list)
# 分割出来的结果为：['#a\n    Trans:art. 一;字母A', 'a.m.\n    Trans:n. 上午', 'aardvark\n    Trans:n. 土猪',
my_dict = {}

# 创建字典
for word in word_list:
    # 去掉#号
    if "#" in word:
        word = word.replace("#", "")
    # 拆分单词和翻译内容
    key, value = word.split("\n    Trans:")
    # 写入字典
    my_dict[key] = value

# 查询字典
user_input = input("请输入要查询的单词：")
if user_input in my_dict:
    print(f"{user_input}的翻译为：{my_dict[user_input]}")
else:
    print("输入的单词字典中未收录！")



