import calendar
import datetime
def dayWeek():
    dateInput = input("Введите дату в формате ГГГГ-ММ-ДД: ")

    try:
        year, month, day = map(int, dateInput.split('-'))

        if year < 1900 or year > datetime.date.today().year:
            print("Год введен некорректно. Год должен быть в пределах от 1900 до текущего года.")
            return
        if month < 1 or month > 12:
            print("Месяц введен некорректно. Месяц должен быть в пределах от 1 до 12.")
            return
        date = datetime.date(year, month, day)
    except ValueError:
        print("Дата введена некорректно. Используйте формат ГГГГ-ММ-ДД.")
        return

    if date > datetime.date.today():
        print("Дата не может превышать сегодняшний день.")
        return

    weekDay = calendar.weekday(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    print(f"День недели для даты {dateInput}: {days[weekDay]}")

dayWeek()
