# 喜欢的数字：使用一个字典来存储一些人喜欢的数字。
# 请想出5个人的名字，并将这些名字用作字典的键；想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。
# 打印每个人的名字和喜欢的数字。

luckyNumbers = {'Jerry': 7, 'Tom': 4, 'Jar': 3, 'Mabel': 4, 'Ham': 9}

for name, num in luckyNumbers.items():
    print('%s喜欢数字 %s' % (name, num))