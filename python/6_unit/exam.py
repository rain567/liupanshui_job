hobbies = {
    91002: ['跳绳', '五子棋', '军棋'],
    91001: ['爬山', '乒乓球', '篮球', '游戏'],
    91005: ['听歌', '看书', '睡觉', '看电影', '跑步'],
    91004: ['钓鱼', '旅游', '骑行', '乐高'],
    91003: ['pc game', 'handheld game', 'host game']
}

for employee_num in sorted(hobbies.keys(), reverse=True):
    print('\n\n工号为{}的爱好是：'.format(employee_num))
    for hobby in hobbies[employee_num]:
        print(hobby, end='、')

