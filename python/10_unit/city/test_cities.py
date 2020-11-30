import unittest
from city_functions import cities_and_countries


class CitiesCase(unittest.TestCase):
    # （2）创建一个名为test_cities.py的程序，对刚编写的函数进行测试。编写一个名为test_city_country()的方法，核实使用类似于'santiago'和'chile'这样的值来调用前述函数时，
    # 得到的字符串是正确的。运行test_cities.py，确认测试test_city_country()通过了。
    def test_city_country(self):
        santiago_chile = cities_and_countries('santiago', 'chile')
        print('santiago_chile', santiago_chile)
        self.assertEqual(santiago_chile, 'Santiago,Chile')

    # （5）再编写一个名为test_city_country_population()的测试，核实可以使用类似于'Santiage'、'Chile'、'population=5000000'这样的值来调用这个函数。
    # 再次运行test_cities.py，确认测试test_city_country_population()通过了。
    def test_city_country_population(self):
        santiago_chile = cities_and_countries('santiago', 'chile', 50000000)
        print('santiago_chile', santiago_chile)
        self.assertEqual(santiago_chile, 'Santiago,Chile-population 50000000')


unittest.main
