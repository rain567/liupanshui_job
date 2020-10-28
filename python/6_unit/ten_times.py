# 10的整数倍：让用户输入一个数字，并指出这个数字是否是10的整数倍。

number = eval(input('请输入一个数字：'))
if number % 10 == 0:
    print('是10的整倍数')
else:
    print('不是10的整倍数')
