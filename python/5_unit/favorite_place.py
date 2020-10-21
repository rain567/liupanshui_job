# 喜欢的地方：创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

favorite_places = {
    'Jerry': ['大理', '香格里拉', '地中海'],
    'Tom': ['西双版纳', '黄果树'],
    'Pack': ['杭州']
}

for name, places in favorite_places.items():
    print('\n%s喜欢的地方' % name, end=':')
    for place in places:
        print(place, end=' ')