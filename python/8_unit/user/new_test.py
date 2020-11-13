#6
from new_user import User
from new_admin import *

user = User('jack','男','20','六盘水')
user.describe_user()
print('\n')

admin = Admin()
admin.privileges.privileges = ['修改','查询','增加']
admin.describe_user()
admin.privileges.show_privileges()

