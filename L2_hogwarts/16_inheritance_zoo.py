#【练习】动物园

# 知识点
# 实例方法、实例属性、类属性、构造方法
# 封装、继承、多态

# 作业要求
# 设计一个简单的动物园系统，其中包含不同类型的动物（如狗、猫和鸟）。
# 每个动物都有自己的属性（如名字、年龄）和行为（如发出声音）。
# 使用封装、继承和多态来完成。

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("发出声音")

class Dog(Animal):
    def __init__(self, age):
        super().__init__("Dog", age)

    def sound(self):
        print("汪汪汪")


class Cat(Animal):
    def __init__(self, age):
        super().__init__("Cat", age)

    def sound(self):
        print("喵喵喵")


class Bird(Animal):
    def __init__(self, age):
        super().__init__("Bird", age)

    def sound(self):
        print("叽叽喳喳")

dog = Dog(2)
cat = Cat(3)
bird = Bird(1)

dog.sound() # 汪汪汪
cat.sound() # 喵喵喵
bird.sound() # 叽叽喳喳
