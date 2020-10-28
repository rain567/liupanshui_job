# 水果拼盘：编写一个循环，提示用户输入一系列的水果名，并在条件不满足时结束循环。
# 每当用户输入一种水果名后，都打印一条消息，说我们会在拼盘中加入这种水果，如"我们会在拼盘中加入桔子"。分别采用如下所有做法：
# （1）在while循环中使用条件测试来结束循环。
# （2）使用变量active来控制循环结束的时机。
# （3）使用break语句在用户输入"quit"时退出循环。

print('（1）在while循环中使用条件测试来结束循环。')
fruits = input('请输入一种水果名：')
while fruits != 'quit':
    print('我们会在拼盘中加入{}'.format(fruits))
    fruits = input('请输入一种水果名：(输入 quit 退出)')

print('\n（2）使用变量active来控制循环结束的时机。')
active = True
while active:
    fruits = input('请输入一种水果名：(输入 quit 退出)')
    if fruits != 'quit':
        print('我们会在拼盘中加入{}'.format(fruits))
    else:
        active = False

print('\n（3）使用break语句在用户输入"quit"时退出循环。')
while True:
    fruits = input('请输入一种水果名：(输入 quit 退出)')
    if fruits == 'quit':
        break
    print('我们会在拼盘中加入{}'.format(fruits))
