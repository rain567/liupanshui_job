# 检查用户名：按照下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二。
# （1）创建一个至少包含5个用户名的列表，并将其命名为 current_users。
# （2）再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
# （3）遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
# （4）确保比较时不区分大小写，如果用户名“John”已被使用，应拒绝用户名“JOHN”。

# （1）创建一个至少包含5个用户名的列表，并将其命名为 current_users。
current_users = ['tom', 'jerry', 'rain', 'admin', 'root']

# （2）再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
new_users = ['tom', 'lob', 'RAIN', 'bol', 'ded']

print('（3）遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息， 指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。')
for user in new_users:
    if user in current_users:
        print(user, '已经被使用, 需要输入用户名')
        continue
    print(user, '未被使用')

print('\n（4）确保比较时不区分大小写，如果用户名“John”已被使用，应拒绝用户名“JOHN”。')
for user in new_users:
    if user.lower() in [current_user.lower() for current_user in current_users]:
        print(user, '已经被使用, 需要输入用户名')
        continue
    print(user, '未被使用')