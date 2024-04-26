import re
def inputData():
    namePattern = r"^[A-Za-zА-Яа-я-]{2,20}$"
    departmentPattern = r"^[A-Za-zА-Яа-я0-9]+( [A-Za-zА-Яа-я0-9]+)?$"
    childrenPattern = r"^[0-9]|1[0-9]$"

    while True:
        firstName = input("Имя сотрудника: ")
        lastName = input("Фамилия сотрудника: ")
        department = input("Отдел: ")
        children = input("Количество детей (0-19): ")

        if not re.match(namePattern, firstName) or not re.match(namePattern, lastName):
            print("Ошибка: Имя и фамилия сотрудника должны содержать от 2 до 20 букв.")
            continue
        if not re.match(departmentPattern, department):
            print("Ошибка: Название отдела должно содержать буквы и цифры.")
            continue
        if not re.match(childrenPattern, children):
            print("Ошибка: Количество детей должно быть числом от 0 до 19.")
            continue

        with open("data.txt", "a") as file:
            file.write(f"{lastName}\t{firstName}\t{department}\t{children}\n")
        print("Данные успешно добавлены.")
        break

def viewChildrenInfo():
    totalChildren = 0
    try:
        with open("data.txt", "r") as file:
            for line in file:
                lastName, firstName, department, children = line.strip().split('\t')
                print(f"{lastName} {firstName}, Отдел: {department}, Детей: {children}")
                totalChildren += int(children)
        print(f"Всего детей у сотрудников: {totalChildren}")
    except FileNotFoundError:
        print("Файл данных не найден.")

def listChildlessEmployees(): 
    try:
        with open("data.txt", "r") as file:
            print("Сотрудники без детей:")
            for line in file:
                lastName, firstName, department, children = line.strip().split('\t')
                if children == '0':
                    print(f"{lastName} {firstName}")
    except FileNotFoundError:
        print("Файл данных не найден.")

def mainMenu():
    while True:
        print("\n1. Ввод данных")
        print("2. Просмотр данных о детях сотрудников")
        print("3. Список бездетных сотрудников")
        print("4. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            inputData()
        elif choice == '2':
            viewChildrenInfo()
        elif choice == '3':
            listChildlessEmployees()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неправильный выбор. Пожалуйста, введите номер опции.")

mainMenu()