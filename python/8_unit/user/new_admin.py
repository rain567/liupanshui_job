from new_user import *
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
