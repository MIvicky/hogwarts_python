#【练习】英雄游戏

# 相关知识点：构造函数、实例对象、实例属性、实例方法
# 需求： 1. 根据英雄类，实例化不同的英雄对象。
# 2. 每个英雄需要在实例化的时候，就有自己的姓名、攻击力、血量

# 相关知识点：封装。
# 需求：每个英雄的血量不可以直接被获取或者修改。
class Hero:
    def __init__(self, name, hp, power):
        self.name = name
        # 私有属性
        self.__hp = hp
        self.power = power

    # 获取hp
    def get_hero_hp(self):
        return self.__hp

    # 讲台词方法
    def speak_lines(self):
        print(f"欢迎来到王者荣耀，我的名字是{self.name}, 我的血量为{self.__hp}")

lvbu = Hero("吕布", 1000, 80)
lvbu.speak_lines()
# 欢迎来到王者荣耀，我的名字是吕布, 我的血量为1000
# print(lvbu.hp)
# AttributeError: 'Hero' object has no attribute 'hp'

# 相关知识点：继承、调用父类属性、父类方法、重写父类属性、方法、super。
# 需求1：现在除了英雄类，还有一种类是法师类。法师类继承于 Hero 类。
# 法师类多了魔力的属性 法师类多了一个放技能的方法。
class APCHero(Hero):
    def __init__(self, name, hp, power, mp):
        super().__init__(name, hp, power)
        self.mp = mp

    def speak_lines(self):
        super().speak_lines()
        print("我是法师")

    def charm(self):
        if self.mp < 50:
            print("蓝量不足")
        else:
            print("施展法术技能")
            self.mp -= 50

diaochan = APCHero("貂蝉", 1200, 80, 70)
diaochan.speak_lines()
# 欢迎来到王者荣耀，我的名字是貂蝉, 我的血量为1200
# 我是法师
diaochan.charm()
# 施展法术技能

# 相关知识点：多态、 类型注解、导包。
# 需求：定义一个单独的 fight 函数。 在打斗之前，需要两个英雄先讲出台词。
# 这个fight函数要求实现两个英雄的多轮回合制对打功能。最后需要返回一个赢家。
def fight(hero1: Hero, hero2: Hero):
    # 在打斗之前，需要两个英雄先讲出台词
    hero1.speak_lines()
    hero2.speak_lines()

    # 实现两个英雄的多轮回合制对打功能。最后需要返回一个赢家。
    hero1_hp = hero1.get_hero_hp()
    hero2_hp = hero2.get_hero_hp()
    hero1_name = hero1.name
    hero2_name = hero2.name

    while True:
        hero1_hp -= 10
        hero2_hp -= 10
        # 当第一个英雄的血量小于0 或 当第二个英雄的血量小于0
        if hero1_hp <= 0 or hero2_hp <= 0:
            if hero1_hp > hero2_hp:
                print(f"英雄{hero1_name}赢了")
                return hero1_name
            elif hero1_hp < hero2_hp:
                print(f"英雄{hero2_name}赢了")
                return hero2_name
            else:
                return "平局"


jinx = Hero("jinx", 1000, 100)
diaochan = APCHero("貂蝉", 1200, 80, 70)
fight(jinx, diaochan)
# 欢迎来到王者荣耀，我的名字是jinx, 我的血量为1000
# 欢迎来到王者荣耀，我的名字是貂蝉, 我的血量为1200
# 我是法师
# 英雄貂蝉赢了

# 设计模式
# 相关知识点： 不定长参数、工厂设计模式、静态方法、类方法
# 需求：现在多了一个同事小林，小林需要调用各种英雄初始化的方法，去完成他自己的逻辑。但是小林并不知道我设计了多少个类型的英雄。
# 所以小林需要我将我目前所有的英雄类都放在一个工厂方法中进行初始化，传入不同的参数信息，返回不同的实例对象。
# 如此一来，小林便不需要了解细节，只需要传入对应的参数获取对应的英雄即可。
class HeroFactory:
    @staticmethod
    def create_hero(hero_type, *args):
        if hero_type == "apc":
            return APCHero(*args)
        elif hero_type == "adc":
            # return ADCHero(*args)
            print("adc")
        else:
            return Hero(*args)
