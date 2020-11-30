import unittest
from hand.employee import Employee


# （2）为Employee编写一个测试用例，其中包含两个测试方法：test_give_default_raise()和test_give_custom_raise()。
# 使用方法setUp()，以免在每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
class EmployeeTest(unittest.TestCase):
    def test_give_default_raise(self):
        annual_salary = self.employee.annual_salary
        self.employee.give_raise()
        self.assertEqual(annual_salary + 5000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        annual_salary = self.employee.annual_salary
        self.employee.give_raise(10000)
        self.assertEqual(annual_salary + 10000, self.employee.annual_salary)

    def setUp(self):
        self.employee = Employee('rain', 20000)


if __name__ == "__main__":
    unittest.main()
