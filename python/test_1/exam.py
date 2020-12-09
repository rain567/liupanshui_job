# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件中保存。
text = str(input('请输入一个字符串：'))
with open('text.txt', 'w') as file:
    file.write(text.upper())
