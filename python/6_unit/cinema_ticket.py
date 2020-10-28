# 电影票：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10元；
# 超过12岁的观众为15元。请编写一个循环，在其中询问用户的年龄，并指出其票价。分别采用如下所有做法：
# （1）在while循环中使用条件测试来结束循环。
# （2）使用变量active来控制循环结束的时机。
# （3）使用break语句在用户输入"quit"时退出循环。

print('（1）在while循环中使用条件测试来结束循环。')
age = eval(input('请问您的年龄是？'))
while age != quit:
    if age < 0 or age > 150:
        print('年龄异常!')
    elif age < 3:
        print('免费')
    elif age <= 12:
        print('票价10元')
    elif age > 12:
        print('票价15元')
    age = eval(input('请问您的年龄是？(输入 quit 退出)'))

print('\n（2）使用变量active来控制循环结束的时机。')
active = True
while active:
    age = eval(input('请问您的年龄是？(输入 quit 退出)'))
    if age == quit:
        active = False
        continue
    elif age < 0 or age > 150:
        print('年龄异常!')
    elif age < 3:
        print('免费')
    elif age <= 12:
        print('票价10元')
    elif age > 12:
        print('票价15元')
#
print('\n（3）使用break语句在用户输入"quit"时退出循环。')
while True:
    age = eval(input('请问您的年龄是？(输入 quit 退出)'))
    if age == quit:
        break
    elif age < 0 or age > 150:
        print('年龄异常!')
    elif age < 3:
        print('免费')
    elif age <= 12:
        print('票价10元')
    elif age > 12:
        print('票价15元')