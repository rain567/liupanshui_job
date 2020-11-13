# 人：设计一个Person（人）类，包括姓名、年龄和血型属性。编写构造方法用于初始化属性值，编写detail方法用于打印输出每个属性值。
# 创建一个Person类的实例，并调用detail方法，打印输出实例的属性值。

class Person:

    def __init__(self, name, age, blood_type) -> None:
        self.name = name
        self.age = age
        self.blood_type = blood_type

    def detail(self):
        print('姓名：{}，年龄：{}岁，血型：{}型'.format(self.name, self.age, self.blood_type))


if __name__ == '__main__':
    tom = Person('tom', 12, 'AB')
    tom.detail()

