# 雇员：（1）编写一个名为Employee的类，其方法__init__()接受姓名、年薪，并将它们都存储在属性中。编写一个名为give_raise()的方法，它默认将年薪增加5000美元，
# 但也能够接受其他的年薪增加量。将这个类存储在一个名为employee.py的模块中。
class Employee:
    def __init__(self, name, annual_salary) -> None:
        self.name = name
        self.annual_salary = annual_salary

    def give_raise(self, add_money=5000):
        self.annual_salary += add_money

