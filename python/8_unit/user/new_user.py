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
