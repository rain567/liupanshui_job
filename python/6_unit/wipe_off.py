# 去除特定值：已知列表locations = ["贵州","云南","贵州","四川","北京","贵州","上海","贵州","广州","贵州"]，
# 将其中所有的"贵州"删除，并打印删除指定值之后的列表。

locations = ["贵州", "云南", "贵州", "四川", "北京", "贵州", "上海", "贵州", "广州", "贵州"]
while '贵州' in locations:
    locations.remove('贵州')

print('删除后的列表：')
for location in locations:
    print(location, end='、')