# （1）在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，其中每一行都以"在Python中可以"打头。
# 将这个文件命名为learning_python.txt，并将其存储到D盘test目录中。
# 编写一个程序，它读取这个文件，并将你所写的内容打印三次；第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with代码块外打印它们。
# （2）使用方法replace()将字符串中的特定单词都替换为另一个单词。读取learning_python.txt文件中的每一行，
# 将其中的Python都替换为另外一门语言的名称，如C。将修改后的各行都打印在屏幕上。

# （1）在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，其中每一行都以"在Python中可以"打头。
# 将这个文件命名为learning_python.txt，并将其存储到D盘test目录中。
# 编写一个程序，它读取这个文件，并将你所写的内容打印三次；第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with代码块外打印它们。
def learning_python_read():
    print('1、读取整个文件：')
    with open('D:/test/learning_python.txt', 'r', encoding='utf-8') as learning_python:
        print(learning_python.read())

    print('\n2、遍历文件对象：')
    with open('D:/test/learning_python.txt', 'r', encoding='utf-8') as learning_python:
        for line in learning_python.readlines():
            print(line.strip('\n'))

    print('\n3、遍历文件对象：')
    file_content_list = []
    with open('D:/test/learning_python.txt', 'r', encoding='utf-8') as learning_python:
        for line in learning_python.readlines():
            file_content_list.append(line.strip('\n'))
    for file_content in file_content_list:
        print(file_content)


# （2）使用方法replace()将字符串中的特定单词都替换为另一个单词。读取learning_python.txt文件中的每一行，
# 将其中的Python都替换为另外一门语言的名称，如C。将修改后的各行都打印在屏幕上。
def learning_python_replace():
    with open('D:/test/learning_python.txt', 'r', encoding='utf-8') as learning_python:
        print(learning_python.read().replace('Python', 'java'))


if __name__ == '__main__':
    # learning_python_read()
    learning_python_replace()

