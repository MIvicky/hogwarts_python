#【练习】购物车

# 知识点
# Python 面向对象

# 作业要求
# 定义一个商品类，包含 商品名称 和 商品价格 两个属性，
# 实现商品类的对象描述方法和添加到购物车方法
# 定义一个购物车类，包含一个商品列表 属性，和 添加商品 及 显示所有商品 两个方法

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 实现商品类的对象描述方法
    def __str__(self):
        return f"商品名称：{self.name}, 商品价格：{self.price}"

    # 添加到购物车方法
    def add_to_shopping_cart(self, shopping_cart):
        # 因为实现了__str__方法，所以传递过去的实例对象self就变成了一个字符串："商品名称：{self.name}, 商品价格：{self.price}"
        shopping_cart.add_product(self)

class ShoppingCart:
    def __init__(self):
        self.product_list = []

    # 添加商品
    def add_product(self, product):
        # product = {"name": product.name, "price": product.price}
        self.product_list.append(product)

    # 显示所有商品
    def show_products(self):
        for item in self.product_list:
            print(item)


# 创建商品对象
product1 = Product("Apple", 5.0)
product2 = Product("Banana", 3.0)
product3 = Product("Orange", 4.0)

print(product1)
# 商品名称：Apple, 商品价格：5.0

# 创建购物车对象
my_cart = ShoppingCart()
# 添加上述三个商品到我的购物车中
product1.add_to_shopping_cart(my_cart)
product2.add_to_shopping_cart(my_cart)
product3.add_to_shopping_cart(my_cart)

# 显示购物车中的所有商品
my_cart.show_products()
# 商品名称：Apple, 商品价格：5.0
# 商品名称：Banana, 商品价格：3.0
# 商品名称：Orange, 商品价格：4.0
