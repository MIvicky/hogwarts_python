# 【练习】闰年
# 输入一个4位年份，判断是否是闰年
# 判断条件：能被4整除但不能被100整除，或能被400整除
# 比如：闰年有：
# 1980, 1984, 1988, 1992, 1996, 2000,
# 2004, 2008, 2012, 2016, 2020, 2024

input_year = int(input("请输入年份："))
is_leap_year = "是闰年" if ((input_year % 4 == 0 and input_year % 100 != 0)
                            or (input_year % 400 == 0))\
                       else "不是闰年"
print(f"{input_year}年{is_leap_year}")