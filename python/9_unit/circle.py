# 设计一个Circle（圆）类，包括半径和颜色属性，编写构造方法和其他方法，计算圆的周长和面积。
# 创建一个Circle类的实例，并调用Circle类的方法，分别计算及打印输出半径为5的圆周长和圆面积。

import math


class Circle:
    def __init__(self, radius, color) -> None:
        self.radius = radius
        self.color = color

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(5, 'red')
    print('圆的周长为： {}'.format(circle.perimeter()))
    print('圆的面积为： {}'.format(circle.area()))

