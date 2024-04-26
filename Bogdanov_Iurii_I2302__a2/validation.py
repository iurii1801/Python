import datetime

def validateDate(dateStr):
    try:
        date = datetime.datetime.strptime(dateStr, '%d.%m.%Y')
        if date.year == 2024 and date <= datetime.datetime.now():
            return True
        else:
            print("Дата должна быть в 2024 году и не позже текущего дня.")
            return False
    except ValueError:
        print("Неверный формат даты. Используйте формат дд.мм.гггг.")
        return False

def validateTime(timeStr):
    try:
        time = datetime.datetime.strptime(timeStr, '%H:%M')
        return True
    except ValueError:
        print("Неверный формат времени. Используйте формат чч:мм.")
        return False

def validateTransactionType(typeStr):
    if typeStr.lower() in ['доход', 'расход']:
        return True
    else:
        print("Тип операции должен быть 'доход' или 'расход'.")
        return False
