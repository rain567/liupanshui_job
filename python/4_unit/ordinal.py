# 序数：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
# （1）在一个列表中存储数字1~9。
nums = list(range(1, 10))

print('（2）遍历这个列表。')
for num in nums:
    print(num)

print('\n（3）在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。输出内容应为# 1st、2nd、3rd、4th、5th、6th、7th、8th和9th。但每个序数都独占一行。')
for num in nums:
    if num > 3:
        print(str(num) + 'th')
    elif num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
