# 访客名单：编写一个while循环，提示用户输入其名字。
# 用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到D盘test目录下的guest_book.txt文件中。确保这个文件中的每条记录都独占一行。

filename = r'D:\test\guest_book.txt'
print("输入'quit'后结束。")
while True:
    name = input("\n输入你的名字： ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("你好 " + name + ", 您已被添加到留言簿中。")