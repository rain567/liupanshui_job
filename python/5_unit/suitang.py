# 课前考试
users = {
    1002: ['python', 'c++', 'java'],
    1001: ['c', 'java', 'mysql'],
    1003: ['.net', 'go', 'js']
}

for user in sorted(users.keys()):
    print('学号：%s，选了' % user, end='：');
    for course in users[user]:
        print(course, end=',')
    print('等课。\n')
