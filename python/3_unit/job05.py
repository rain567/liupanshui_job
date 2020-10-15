# 奇数：通过给函数range()指定第三个参数来创建一个列表，
# 其中包含1~20的奇数；再使用一个for循环将这些数字都打印出来。
odd_nums = range(1, 20, 2)
for odd_num in odd_nums:
    print(odd_num, end=',')