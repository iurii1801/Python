def addAuthor(infoAuthorsBooks):
    author = input("Введите фамилию автора: ")
    if author in infoAuthorsBooks:
        print("Этот автор уже есть.")
    else:
        infoAuthorsBooks[author] = []
        print("Автор добавлен.")
    return infoAuthorsBooks


def addBook(infoAuthorsBooks):
    author = input("Введите автора книги: ")
    if author not in infoAuthorsBooks:
        print("Этого автора нет.")
    else:
        books = input("Введите название книги: ")
        infoAuthorsBooks[author].append(books)
        print("Книга добавлена.")
    return infoAuthorsBooks


def viewAuthors(infoAuthorsBooks):
    print("Список авторов и их книг:")
    for author, books in infoAuthorsBooks.items():

        print(author + ": " + ", ".join(books))


def viewBooksCount(infoAuthorsBooks):
    print("Количество книг у каждого автора:")
    for author, books in infoAuthorsBooks.items():
        print(author + ": " + str(len(books)))


def deleteAuthor(infoAuthorsBooks):
    author = input("Введите фамилию автора, которого хотите удалить: ")
    if author in infoAuthorsBooks:
        del infoAuthorsBooks[author]
        print("Автор удален.")
    else:
        print("Этого автора нет.")
    return infoAuthorsBooks