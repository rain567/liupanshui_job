# 定制水果拼盘：编写一个函数，它接受顾客要定制的水果拼盘的大小，以及要在水果拼盘中添加的一系列水果。
# 并打印一条消息，如：“您的水果拼盘为10寸，里包含的水果有：苹果  桔子  香蕉  芒果”调用这个函数三次，每次都提供不同数量的实参。

def make_fresh_fruit(size, *fruits):
    print('\n您的水果拼盘为{}寸，里包含的水果有：'.format(size), end='')
    for fruit in fruits:
        print(fruit, end='\t')


make_fresh_fruit(10, '香蕉', '橘子')
make_fresh_fruit(15, '苹果', '猕猴桃', '西瓜')
make_fresh_fruit(20, '黄桃', '哈密瓜', '芒果', '桃子')