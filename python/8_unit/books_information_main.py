import books_information

book_information = books_information.books_profile('长日将尽', ['石黑一雄'], '第二版', 出版社='长江出版社')
for k, v in book_information.items():
    if k == '作者':
        print('{}:'.format(k), end='')
        for author in v:
            print(author, end=',')
        print()
    else:
        print('{}：{}'.format(k, v))