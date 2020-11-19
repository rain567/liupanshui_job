print("输入 ' quit ' 退出！")
while True:
    try:
        number_1 = input("请输入第一个数字：")
        if number_1 == 'quit':
            break
        number_1 = int(number_1)
        number_2 = input("请输入第二个数字：")
        if number_2 == 'quit':
            break
        number_2 = int(number_2)
    except ValueError:
        print("抱歉，请您输入数字！")
    else:
        sum_number = number_1 + number_2
        print("数字'{}'与'{}'相加等于'{}'".format(number_1, number_2, sum_number))