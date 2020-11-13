# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print('餐馆名称:{}'.format(self.restaurant_name))
#         print('餐馆类型:{}'.format(self.cuisine_type))
#
#     def open_restaurant(self):
#         print('{}餐馆营业中，欢迎光临！'.format(self.restaurant_name))
#
#
# print('(1）根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。')
# if __name__ == '__main__':
#     restaurant = Restaurant('川川', '川菜馆')
#     print('餐馆名称1:{}'.format(restaurant.restaurant_name))
#     print('餐馆类型1:{}'.format(restaurant.cuisine_type))
#     restaurant.describe_restaurant()
#     restaurant.open_restaurant()
#
#
# print('\n(2）根据这个类创建三个实例，并对每个实例调用方法describe_restaurant()')
# if __name__ == '__main__':
#     restaurant_1 = Restaurant('月月', '粤菜')
#     restaurant_2 = Restaurant('串串', '川菜')
#     restaurant_3 = Restaurant('汤', '鲁菜')
#     restaurant_1.describe_restaurant()
#     restaurant_2.describe_restaurant()
#     restaurant_3.describe_restaurant()
#
# print('\n（3）在Restaurant类中添加一个名为number_served的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。')
# if __name__ == '__main__':
#     restaurant = Restaurant('串串', '川菜')
#     print('就餐人数为：', restaurant.number_served)
#     restaurant.number_served = 20
#     print('就餐人数为：', restaurant.number_served)
#
#
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print('餐馆名称:{}'.format(self.restaurant_name))
#         print('餐馆类型:{}'.format(self.cuisine_type))
#
#     def open_restaurant(self):
#         print('{}餐馆营业中，欢迎光临！'.format(self.restaurant_name))
#
#     def set_number_served(self, number):
#         self.number_served = number
#
#
# print('（4）继续添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。')
# if __name__ == '__main__':
#     restaurant = Restaurant('串串', '川菜')
#     restaurant.set_number_served(27)
#     print('就餐人数为：', restaurant.number_served)
#

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('餐馆名称:{}'.format(self.restaurant_name))
        print('餐馆类型:{}'.format(self.cuisine_type))

    def open_restaurant(self):
        print('{}餐馆营业中，欢迎光临！'.format(self.restaurant_name))

    def set_number_served(self, number):
        self.number_served = number

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_server(self, number):
        self.number_served += number


# print('（5）继续添加一个名为increment_number_server()方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个你认为这家餐馆每天可能接待的就餐人数的值，然后再次打印这个值。')
if __name__ == '__main__':
    restaurant = Restaurant('串串', '川菜')
    # restaurant.increment_number_server(27)
    # print('就餐人数为：', restaurant.number_served)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='冰淇淋店'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def print_varieties(self):
       print('冰淇淋的口味有：', end='')
       for i in self.flavors:
           print(i, end=' ')


print('6）冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承Restaurant类。添加一个名为 flavors的属性，'
      '用于存储这个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法print_varieties()。创建IceCreamStand实例，'
      '并调用父类describe_restaurant()方法和子类print_varieties()方法。')
if __name__ == '__main__':
    ice_cream_stand = IceCreamStand('ice cream')
    ice_cream_stand.flavors = ['蓝莓', '红桃', '草莓']
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.print_varieties()
