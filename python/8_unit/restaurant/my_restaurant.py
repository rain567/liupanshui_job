class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('餐馆名称:', self.restaurant_name)
        print('餐馆类型:', self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + '餐馆营业中，欢迎光临！')

    def set_number_served(self,number):
        self.number_served = number
