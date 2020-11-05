# 朋友：（1）创建一个包含朋友名字的列表，并将其传递给一个名为show_friends()的函数，这个函数打印列表中每个朋友的名字。
# （2）编写一个名为make_great()的函数，对朋友列表进行修改，在每个朋友的名字后都加入“超棒” 字样。调用函数show_friends()，确认朋友列表确实变了。
# （3）在调用函数make_great()时，向它传递朋友列表的副本。由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
# 分别使用这两个列表来调用show_friends()，确认一个列表包含的是原来的朋友名字，而另一个列表包含的是添加了字样“超棒”的朋友名字。


def show_friends(friend_list):
    for friend in friend_list:
        print(friend, end='\t')
    print()


def make_great(friend_list):
    for index in range(len(friend_list)):
        friend_list[index] = friend_list[index] + '超棒'
    return friend_list


friends = ['tom', 'jerry', 'rain']
show_friends(friends)
# 添加字样并创建为新列表
new_friends = make_great(friends.copy())
show_friends(new_friends)


