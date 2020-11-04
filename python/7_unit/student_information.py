# 打印模型：编写一个名为student_profile()的函数，将学生信息存储在一个字典中。这个函数总是接受学号、姓名、性别，且性别给定默认值“女”。
# 还接受任意数量的用于描述学生个人信息（如：班级、手机号、生源地等）的关键字实参。
# 将此函数制作成名为student_information的模型，在主程序文件中，从student_message模型中导入这个函数，再调用它，并打印学生信息。

def student_profile(stu_num, stu_name, stu_sex='女', **information):
    stu = {'学号': stu_num, '姓名': stu_name, '性别': stu_sex}
    stu.update(information)
    return stu

