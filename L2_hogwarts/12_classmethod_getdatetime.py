import datetime

# 封装一个获取日期时间的工具类
class Utils:
    now = datetime.datetime.now()

    @classmethod
    def current_date_time(cls):
        return cls.now

    @classmethod
    def current_date(cls):
        return cls.now.strftime("%Y-%m-%d")

    @classmethod
    def current_time(cls):
        return cls.now.strftime("%H:%M:%S")

    @classmethod
    def getYear(cls):
        return cls.now.year

    @classmethod
    def getMonth(cls):
        return cls.now.month

    @classmethod
    def getDay(cls):
        return cls.now.day


print(Utils.current_date_time()) # 2024-08-08 21:56:53.176959
print(Utils.current_date()) # 2024-08-08
print(Utils.current_time()) # 21:56:53
print(Utils.getYear()) # 2024
print(Utils.getMonth()) # 8
print(Utils.getDay()) # 8
