#【练习】面向对象跑步减肥

# 知识点
# 类、实例、构造方法、实例属性

# 作业要求
# 小明和小美都爱跑步
# 小明体重 75 公斤
# 小美体重 45 公斤
# 每次跑步会减肥 0.5 公斤
# 每次吃东西体重增加 1 公斤
# 请根据信息打印出跑完步之后的体重

class RunForLossWeight:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # 每次跑步会减肥 0.5 公斤
    def running(self):
        print(f"{self.name} 在跑步，体重减少0.5公斤")
        self.weight -= 0.5

    # 每次吃东西体重增加 1 公斤
    def eating(self):
        print(f"{self.name} 在吃饭，体重增加1公斤")
        self.weight += 1

    def __str__(self):
        return f"{self.name} 很爱跑步，目前的体重是：{self.weight} 公斤"

xiao_ming = RunForLossWeight("小明", 75)
xiao_mei = RunForLossWeight("小美", 45)

print(xiao_ming)
xiao_ming.eating()
xiao_ming.running()
print(xiao_ming)
# 小明 很爱跑步，目前的体重是：75 公斤
# 小明 在吃饭，体重增加1公斤
# 小明 在跑步，体重减少0.5公斤
# 小明 很爱跑步，目前的体重是：75.5 公斤

print(xiao_mei)
xiao_mei.eating()
xiao_mei.running()
xiao_mei.running()
xiao_mei.running()
print(xiao_mei)
# 小美 很爱跑步，目前的体重是：45 公斤
# 小美 在吃饭，体重增加1公斤
# 小美 在跑步，体重减少0.5公斤
# 小美 在跑步，体重减少0.5公斤
# 小美 在跑步，体重减少0.5公斤
# 小美 很爱跑步，目前的体重是：44.5 公斤