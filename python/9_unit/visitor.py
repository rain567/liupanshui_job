# 访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到D盘test目录下的guest.txt文件中。

name = input('请输入名字：')
with open('D:/test/guest.txt', 'w') as guest:
    guest.write(name)