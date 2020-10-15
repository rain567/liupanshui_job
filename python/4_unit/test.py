# 对于下面列出的各种测试，至少编写一个结果为True或False的测试。

print('\n（1）检查两个字符串相等和不等。')
str1 = 'ss'
str2 = 'SS'
if str1 == str2:
    print('相等')
else:
    print('不相等')

print('\n（2）使用函数lower()的测试。')
if str1.lower() == str2.lower():
    print('小写相等')
else:
    print('小写不相等')

print('\n（3）检查两个数字相等、不等、大于、小于、大于等于和小于等于。')
print('数字相等：' + str(10 == 12))
print('数字不等:' + str(10 != 12))
print('数字大于:' + str(10 > 12))
print('数字小于:' + str(10 < 12))
print('数字小于等于:' + str(10 <= 12))
print('数字大于等于:' + str(10 >= 12))

print('\n（4）使用关键字and和or的测试。')
print('大于且等于' + str(10 > 12 & 10 == 10))
print('大于或等于' + str(10 > 12 | 10 == 12))

print('\n（5）测试特定的值是否包含在列表中。')
strings = ['str1', 'str2']
print('str1是否包含：' + str('str1' in strings))

print('\n（6）测试特定的值是否未包含在列表中。')
print('str1是否不包含：' + str('str1' not in strings))
