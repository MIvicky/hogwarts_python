#【练习】矩形面积和周长

# 知识点
# 静态方法
# 函数返回值与参数处理

# 作业要求
# 编写一个Python程序，创建一个几何图形计算程序，使用静态方法来计算矩形的面积和周长。
class CalRectangle:
    @staticmethod
    def area(height, width):
        return height * width

    @staticmethod
    def perimeter(height, width):
        return height*2 + width*2

print(f"矩形的面积：{CalRectangle.area(5, 6)}")
# 矩形的面积：30
print(f"矩形的周长：{CalRectangle.perimeter(5, 6)}")
# 矩形的周长：22