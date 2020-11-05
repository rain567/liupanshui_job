# 编写程序，实现判断用户输入账号、密码是否正确。如果账号和密码都正确，就显示“欢迎登录！”，否则，显示账号或密码输入有误，并让用户再次输入，当输入次数超过3次时，显示“已超过最大输入次数！”，并退出程序。

users = {
    'admin': {'username': 'admin', 'password': 'admin'},
    'user1': {'username': 'user1', 'password': '123'},
    'user2': {'username': 'user2', 'password': '123'}
}

i = 2
while True:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    user = users.get(username)
    if user and password == user['password']:
        print('欢迎登录！')
        break

    if i == 0:
        print('已超过最大输入次数')
        break

    print('显示账号或密码输入有误,还有{}次机会'.format(i))

    i = i - 1

