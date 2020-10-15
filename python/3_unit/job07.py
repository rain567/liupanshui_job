# 你的饺子和我的饺子：已知favorite_dumplings = ['鲜肉', '韭菜', '粉条']，
# 创建favorite_dumplings列表的副本，并将其存储到变量friend_dumplings中，再完成如下任务：
# （1）在原来的饺子列表中添加另一种饺子。
# （2）在列表friend_dumplings中添加另一种饺子。
# （3）核实你有两个不同的列表。为此，打印消息“我最喜欢的饺子馅有：”，再使用一个for循环来打印第一个列表；
# 打印消息“我朋友最喜欢的饺子馅有：”，再使用一个for循环来打印第二个列表。核实新增的饺子被添加到了正确的列表中。

favorite_dumplings = ['鲜肉', '韭菜', '粉条']
friend_dumplings = favorite_dumplings.copy()

# （1）在原来的饺子列表中添加另一种饺子。
favorite_dumplings.append('牛肉')

# （2）在列表friend_dumplings中添加另一种饺子。
friend_dumplings.append('鸡肉')

# （3）核实你有两个不同的列表。为此，打印消息“我最喜欢的饺子馅有：“， 再使用一个for循环来打印第一个列表；
print('我最喜欢的饺子馅有：')
for favorite_dumpling in favorite_dumplings:
    print(favorite_dumpling, end=',')

# 打印消息“我朋友最喜欢的饺子馅有：”，再使用一个for循环来打印第二个列表。核实新增的饺子被添加到了正确的列表中。
print('\n\n我朋友最喜欢的饺子馅有：')
for friend_dumpling in friend_dumplings:
    print(friend_dumpling, end=',')

