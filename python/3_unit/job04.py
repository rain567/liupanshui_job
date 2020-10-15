#   3的倍数：创建一个列表，其中包含3~30内能够被3整除的数字；
#   再使用一个for循环将这个列表中的数字都打印出来。

nums = [i * 3 for i in range(1, 11)]
for num in nums:
    print(num, end=',')