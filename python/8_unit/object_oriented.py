# 通过面向对象程序设计方法，设计程序输出如下信息：
# 丽丽，10岁，女，喜欢上语文课
# 丽丽，10岁，女，喜欢看电影
# 丽丽，10岁，女，喜欢打蓝球
# 强强，12岁，男，喜欢上语文课
# 强强，12岁，男，喜欢看电影
# 强强，12岁，男，喜欢打蓝球


class User:

    def __init__(self, name, age, sex, *hobbes) -> None:
        self.name = name
        self.age = age
        self.sex = sex
        self.hobbes = list(hobbes)

    def print_user(self):
        for course in self.hobbes:
            print('{}, {}岁, {}, 喜欢{}'.format(self.name, self.age, self.sex, course))


if __name__ == '__main__':
    ll = User('丽丽', 10, '女', '上语文课', '看电影', '打篮球')
    qq = User('强强', 10, '女', '上语文课', '看电影', '打篮球')

    ll.print_user()
    qq.print_user()

