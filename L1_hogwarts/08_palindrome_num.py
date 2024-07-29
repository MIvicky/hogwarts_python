#【练习】回文数(切片实现)
# 编写一个Python程序，输入一个5位数，判断输入的这个数字是否为回文数。
# 回文数是指从左到右和从右到左读都一样的数。例如12321。
# 如果输入的是回文数，输出是回文数，否则输出不是回文数。

# 字符串切片
str1 = "ABCDEFG"
print(1, str1[1:5:2]) # BD
print(2, str1[1:5:-2]) # ""
print(3, str1[1:5:-1]) # ""
print(4, str1[-5:-1:2]) # CE
print(5, str1[-5:-1:-2]) # ""
print(6, str1[-5:-1:-1]) # ""
# 从某个字符开始倒序输出前面的字符串 str[x::-1]
# 省略x就代表从末尾开始倒序输出整个字符串
print(7, str1[-5::-1]) # CBA
print(8, str1[-3::-1]) # EDCBA
print(9, str1[4::-1]) # EDCBA
print(10, str1[::-1]) # GFEDCBA
print(11, str1[::-2]) # GECA
print(12, str1[-1:-6:-1]) # GFEDC
print(13, str1[-1:-6:-2]) # GEC
print(14, str1[6:1:-1]) # GFEDC
print(15, str1[6:1:-2]) # GEC


# 作业实现
num = input("请输入一个五位数：")
if num == num[::-1]:
    print(f"{num}是回文数")
else:
    print(f"{num}不是回文数")




