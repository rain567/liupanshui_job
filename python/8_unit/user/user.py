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
















      
