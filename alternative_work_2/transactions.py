from validation import validateDate, validateTime, validateTransactionType

def writeTransaction(date, time, amount, transType, filePath):
    if validateDate(date) and validateTime(time) and validateTransactionType(transType):
        try:
            amount = float(amount)
        except ValueError:
            print("Сумма транзакции должна быть числом.")
            return False
        with open(filePath, 'a') as file:
            file.write(f"{date} {time} {amount} {transType}\n")
            return True
    return False

def calculateBalance(filePath):
    balance = 0
    try:
        with open(filePath, 'r') as file:
            for line in file:
                parts = line.strip().split()
                amount = float(parts[2])
                transType = parts[3]
                if transType == 'доход':
                    balance += amount
                elif transType == 'расход':
                    balance -= amount
    except FileNotFoundError:
        print("Файл данных не найден.")
    return balance

def findExtremes(filePath):
    maxTransaction = None
    minTransaction = None
    try:
        with open(filePath, 'r') as file:
            for line in file:
                parts = line.strip().split()
                date, time, amount, transType = parts[0], parts[1], float(parts[2]), parts[3]
                if transType == 'доход' and (maxTransaction is None or amount > maxTransaction[2]):
                    maxTransaction = (date, time, amount, transType)
                if transType == 'расход' and (minTransaction is None or amount > minTransaction[2]):
                    minTransaction = (date, time, amount, transType)
    except FileNotFoundError:
        print("Файл данных не найден.")
    return maxTransaction, minTransaction
