

def books_profile(name, authors, edition='第一版', **information):
    book_information = {
        '书名': name,
        '作者': authors,
        '版次': edition
    }
    book_information.update(information)
    return book_information
