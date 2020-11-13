#1
class User():
    def __init__(self,name,gender,age,address):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address

    def describe_user(self):
        print('姓名：',self.name.title())
        print('性别：',self.gender.title())
        print('年龄：',self.age.title())
        print('家庭住址：',self.address.title())

    def great_user(self):
        print('欢迎您,' + self.name.title() + '!')


if __name__ == '__main__':
    user_1 = User('joe','男','18','六盘水市钟山区')
    user_1.describe_user()
    user_1.great_user()
    print('\n')
    user_2 = User('jmary','女','20','六盘水市盘州')
    user_2.describe_user()
    user_2.great_user()
    
print('\n')

#2
class User():
    def __init__(self,name,gender,age,address):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address
        self.login_attempts = 0

    def describe_user(self):
        print('姓名：',self.name.title())
        print('性别：',self.gender.title())
        print('年龄：',self.age.title())
        print('家庭住址：',self.address.title())

    def great_user(self):
        print('欢迎您,' + self.name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

if __name__ == '__main__':
    user = User('joe','男','18','六盘水市钟山区')
    for i in range(10):
        user.increment_login_attempts()
    print('登陆次数:',user.login_attempts)
    print('\n')
    user.reset_login_attempts()
    print('登陆次数:',user.login_attempts)
print('\n')

#3
class Admin(User):
    def __init__(self,name = 'Rengzz',gender='男',age='18',address='六盘水市六枝'):
        super().__init__(name,gender,age,address)
        self.privileges = []

    def show_privileges(self):
        print('管理员的权限有：',end = '')
        for i in self.privileges:
            print(i,end = ' ')

if __name__ == '__main__':
    admin = Admin(address = '贵阳')
    admin.privileges = ['添加','删除','更新']
    admin.describe_user()
    admin.show_privileges()

print('\n')


#4
class Privileges():
    def __init__(self,privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print('管理员的权限有：',end = '')
        for i in self.privileges:
            print(i,end = ' ')
            
class Admin(User):
    def __init__(self,name = 'Rengzz',gender='男',age='18',address='六盘水市六枝'):
        super().__init__(name,gender,age,address)
        self.privileges = Privileges()

if __name__ == '__main__':
    admin = Admin()
    admin.privileges.privileges = ['查询','删除','更新']
    admin.privileges.show_privileges()
    
















      
