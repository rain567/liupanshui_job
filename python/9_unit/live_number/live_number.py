# 喜欢的数字：
# （1）编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“我知道你最喜欢的数字，是.......。”。
# （2）将前题的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。
import json
import os


# （1）编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
def function_write():
    num = eval(input('请输入喜欢的数字：'))
    with open('data.json', 'w') as json_file:
        json.dump(num, json_file)


def function_read():
    with open('data.json', 'r') as json_file:
        print('我知道你最喜欢的数字，是：{}'.format(json_file.read()))


# （2）将前题的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。
def function_read_fo_write():
    # 判断文件行数
    if os.path.getsize('data.json') > 0:
        with open('data.json', 'r') as json_file:
            print('我知道你最喜欢的数字，是：{}'.format(json_file.read()))
        return

    num = eval(input('请输入喜欢的数字：'))
    with open('data.json', 'w') as json_file:
        json.dump(num, json_file)


if __name__ == '__main__':
    # function_write()
    # function_read()
    function_read_fo_write()
    function_read_fo_write()
