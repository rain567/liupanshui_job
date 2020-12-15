# 有两个文件A和B，各存放一行字母，要求把这两个文件中的信息合并，输出到一个新文件C中。

with open('A', 'r') as a_file:
    with open('B', 'r') as b_file:
        with open('C', 'w') as c_file:
            c_file.write(a_file.read() + '\n')
            c_file.write(b_file.read())

