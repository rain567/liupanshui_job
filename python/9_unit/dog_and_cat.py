# 猫和狗：在D盘test目录下创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# （1）编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except代码块中，
# 以便在文件不存在时捕获FileNotFound错误，并打印一条友好的消息。将其中一个文件移动另一个地方，并确认except代码块中的代码将正确的执行。
# （2）修改前题编写的程序代码中的except代码块，让程序在文件不存在时一言不发。

# （1）编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except代码块中，
# 以便在文件不存在时捕获FileNotFound错误，并打印一条友好的消息。将其中一个文件移动另一个地方，并确认except代码块中的代码将正确的执行。
def file_write(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('文件不存在')


# （2）修改前题编写的程序代码中的except代码块，让程序在文件不存在时一言不发。
def file_write_no_hint(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    # file_write('D:/test/cats.txt')
    # print()
    # file_write('D:/test/dogs.txt')
    # print()
    # # 假装移动文件后
    # file_write('D:/test/dogs1.txt')

    file_write_no_hint('D:/test/dogs1.txt')
