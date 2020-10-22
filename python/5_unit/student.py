# 编写程序，使用字典存储学生信息，学生信息包括学号和姓名，请根据学生学号，从大到小输出学生的信息。
dicts = {
    1001: {'stu_num': 1001, 'name': 'test1'},
    1002: {'stu_num': 1002, 'name': 'test2'},
    1003: {'stu_num': 1003, 'name': 'test3'}
}

for stu_num in sorted(dicts.keys(), reverse=False):
    print('学号：%s，姓名：%s' % (dicts[stu_num]['stu_num'], dicts[stu_num]['name']))