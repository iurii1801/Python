
import functions as func

infoAuthorsBooks = {}

while True:
    print("\nМеню управления")
    print("1. Добавить нового автора")
    print("2. Добавить книгу к существующему автору")
    print("3. Просмотреть список авторов и их книг")
    print("4. Вывести количество книг у каждого автора")
    print("5. Удалить автора и его книги")
    print("6. Выход")

    choice = input("Выберите опцию: ")

    if choice == "1":
        infoAuthorsBooks = func.addAuthor(infoAuthorsBooks)
    elif choice == "2":
        infoAuthorsBooks = func.addBook(infoAuthorsBooks)
    elif choice == "3":
        func.viewAuthors(infoAuthorsBooks)
    elif choice == "4":
        func.viewBooksCount(infoAuthorsBooks)
    elif choice == "5":
        infoAuthorsBooks = func.deleteAuthor(infoAuthorsBooks)
    elif choice == "6":
        print("До свидания!")
        break
    else:
        print("Вы выбрали несуществующую опцию! Выберите из существующих.")

