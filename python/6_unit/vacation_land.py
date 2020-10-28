# 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“如果让你选择参观世界上的一个地方，那么你会选哪里？”的提示，
# 并编写一个打印调查结果的代码块。

vacation_lands = {}

while True:
    print('如果让你选择参观世界上的一个地方，那么你会选哪里？')
    user = input('用户：')
    place = input('地方：')
    vacation_lands[user] = place
    flag = eval(input('请问还需要继续调查吗？(True, False)'))
    if not flag:
        break

for name, place in vacation_lands.items():
    print('{}想去{}'.format(name, place))


