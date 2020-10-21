# 调查：创建一个字典，在其中存储四个人喜欢的编程语言。其中一个键-值对可能是"wangyang":"Python"。
# （1）创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# （2）遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。

survey = {'Tom': 'Java', 'Jerry': 'Python', 'Hal': 'C', 'Earl': 'GO'}
names = ['Cain', 'Jerry', 'Rain', 'Tom', 'Pace']


for name in names:
    if name in survey.keys():
        print('%s 感谢参与调查' % name)
    else:
        print('%s 您好，能来参加一起调查吗？' % name)