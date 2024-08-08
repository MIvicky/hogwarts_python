#【练习】房子家具管理系统

# 知识点
# 对象的封装
# 类的构造方法和实例属性
# for循环

# 作业要求
# 编写一个Python程序：
# 1.房子有户型，总面积和家具名称列表，新房子没有任何的家具。
# 2.家具有名字和占地面积，其中 - 床：占4平米 - 衣柜：占2平米 - 餐桌：占1.5平米
# 3.将以上三件家具添加到房子中
# 4.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

class HouseFurnitureManage:
    def __init__(self, house_type, house_area):
        self.house_type = house_type
        self.house_area = house_area
        self.furniture = []
        self.remain_area = self.house_area

    # 添加家具到房子中
    def add_furniture(self, fur_name, fur_area):
        if self.remain_area < fur_area:
            print(f"抱歉！房子剩余面积不足，无法添置此家具！")
        else:
            fur = {"fur_name":fur_name, "fur_area":fur_area}
            self.furniture.append(fur)
            self.remain_area -= fur_area

    def __str__(self):
        return (f"户型：{self.house_type}\n"
                f"总面积：{self.house_area} 平米\n"
                f"剩余面积：{self.remain_area} 平米\n"
                f"家具名称列表：{[fur['fur_name'] for fur in self.furniture]}")

my_house = HouseFurnitureManage("三室两厅两卫", 146)
my_house.add_furniture("床", 4)
my_house.add_furniture("衣柜", 2)
my_house.add_furniture("餐桌", 1.5)
print(my_house)
# 户型：三室两厅两卫
# 总面积：146
# 剩余面积：138.5
# 家具名称列表：['床', '衣柜', '餐桌']