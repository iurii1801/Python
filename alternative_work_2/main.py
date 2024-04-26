from transactions import writeTransaction, calculateBalance, findExtremes

def mainMenu():
    while True:
        print("\n1. Записать данные о транзакции")
        print("2. Вывести текущий баланс")
        print("3. Вывести самую прибыльную транзакцию")
        print("4. Вывести самую убыточную транзакцию")
        print("5. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            date = input("Введите дату (дд.мм.гггг): ")
            time = input("Введите время (чч:мм): ")
            amount = input("Введите сумму транзакции: ")
            transType = input("Введите тип операции (доход/расход): ")
            if writeTransaction(date, time, amount, transType, 'transactions.txt'):
                print("Транзакция записана.")
            else:
                print("Ошибка в данных транзакции.")
        elif choice == '2':
            balance = calculateBalance('transactions.txt')
            print(f"Текущий баланс: {balance}")
        elif choice == '3':
            transactions = findExtremes('transactions.txt')
            maxTransaction = transactions[0]
            if maxTransaction:
                print("Самая прибыльная транзакция:", " ".join(map(str, maxTransaction)))
            else:
                print("Нет данных или нет прибыльных транзакций.")
        elif choice == '4':
            transactions = findExtremes('transactions.txt')
            minTransaction = transactions[1]
            if minTransaction:
                print("Самая убыточная транзакция:", " ".join(map(str, minTransaction)))
            else:
                print("Нет данных или нет убыточных транзакций.")
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверная опция. Пожалуйста, выберите одну из предложенных опций.")

if __name__ == "__main__":
    mainMenu()
