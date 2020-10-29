hobbies = {
    1002: ['象棋', '五子棋', '围棋'],
    1001: ['羽毛球', '乒乓球', '篮球'],
    1005: ['听歌', '看书', '睡觉'],
    1004: ['钓鱼', '旅游', '骑行'],
    1003: ['pc game', 'handheld game', 'host game']
}

for employee_num in sorted(hobbies.keys(), reverse=True):
    print('\n\n工号{}的爱好是：'.format(employee_num))
    for hobby in hobbies[employee_num]:
        print(hobby, end='、')