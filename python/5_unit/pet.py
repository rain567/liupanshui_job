# 宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；
# 在每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。

cream = {'name': 'cream', 'type': 'cat', 'master': 'Anstey'}
ulrica = {'name': 'ulrica', 'type': 'dog', 'master': 'Jasmine'}
claudia = {'name': 'claudia', 'type': 'cat', 'master': 'Jason'}

pets = [cream, ulrica, claudia]

for pet in pets:
    print('%s的类型是%s，它的主人是%s。' % (pet['name'], pet['type'], pet['master']))