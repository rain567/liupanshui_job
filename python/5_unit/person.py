# 人：使用一个字典来存储一个熟人的信息，包括姓名、年龄、电话和居住的城市，该字典应包含键name、age、phone和city。
# 再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。

people = [
    {'name': 'Jerry', 'age': 19, 'phone': 17777777777, 'city': '六盘水'},
    {'name': 'Tom', 'age': 20, 'phone': 18888888888, 'city': '六盘水'},
    {'name': 'Hal', 'age': 31, 'phone': 13555555555, 'city': '六盘水'}
]

for p in people:
    print('姓名：%s，年龄：%s，电话：%s，地址：%s' % (p['name'], p['age'], p['phone'], p['city']))