users = {
    'admin': {'username': 'admin', 'password': 'admin', 'is_root': True},
    'user1': {'username': 'user1', 'password': '123', 'is_root': False},
    'user2': {'username': 'user2', 'password': '123', 'is_root': False}
}

i = 2
while i >= 0:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    user = users.get(username)
    if not user:
        print('用户不存在!')
        continue
    elif password != user['password']:
        print('密码错误，还有{}次机会'.format(i))
    else:
        if user['is_root']:
            print('管理员 登陆成功')
        else:
            print('{} 登陆成功'.format(username))
        break
    i = i - 1
