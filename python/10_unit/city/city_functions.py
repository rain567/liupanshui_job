# 城市和国家：
# （1）编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为City，Country的字符串，如Santiage,Chile。将这个函数存储在一个名为city_functions.py的模块中。
# （2）创建一个名为test_cities.py的程序，对刚编写的函数进行测试。编写一个名为test_city_country()的方法，核实使用类似于'santiago'和'chile'这样的值来调用前述函数时，
# 得到的字符串是正确的。运行test_cities.py，确认测试test_city_country()通过了。
# （3）修改第（1）题中的函数，使其包含第三个必不可少的形参population， 并返回一个格式为City，Country-population ***的字符串，如Santiage,Chile-population 5000000。
# 运行test_cities.py，确认测试test_city_country()未通过。
# （4）修改第（3）题中的函数，将形参population设置为可选的。再次运行test_cities.py，确认测试test_city_country()又通过了。
# （5）再编写一个名为test_city_country_population()的测试，核实可以使用类似于'Santiage'、'Chile'、'population=5000000'这样的值来调用这个函数。
# 再次运行test_cities.py，确认测试test_city_country_population()通过了。

# （1）编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为City，Country的字符串，如Santiage,Chile。将这个函数存储在一个名为city_functions.py的模块中。
# def cities_and_countries(cities, countries):
#     return '{},{}'.format(cities, countries).title()

# （3）修改第（1）题中的函数，使其包含第三个必不可少的形参population， 并返回一个格式为City，Country-population ***的字符串，如Santiage,Chile-population 5000000。
# 运行test_cities.py，确认测试test_city_country()未通过。
# def cities_and_countries(cities, countries, population):
#     return '{},{}-population {}'.format(cities,
#                                         countries,
#                                         population
#                                         ).title()

# （4）修改第（3）题中的函数，将形参population设置为可选的。再次运行test_cities.py，确认测试test_city_country()又通过了。
def cities_and_countries(cities, countries, population=()):
    returned_value = '{},{}'.format(cities, countries).title()
    if population:
        returned_value += '-population {}'.format(population)
    return returned_value

