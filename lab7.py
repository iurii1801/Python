import datetime
import calendar
import math
import re

def calculateAgeInDays():
    datePattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    birthDateStr = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
    match = re.match(datePattern, birthDateStr)
    if not match:
        print("Дата введена некорректно.")
        return

    year, month, day = map(int, match.groups())
    try:
        birthDate = datetime.date(year, month, day)
    except ValueError as e:
        print(f"Ошибка при создании даты: {e}")
        return

    currentDate = datetime.date.today()
    ageInDays = (currentDate - birthDate).days
    print(f"Прожито дней: {ageInDays}")

calculateAgeInDays()


def findWeekdayOfDate():
    datePattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    dateStr = input("Введите дату (ГГГГ-ММ-ДД): ")
    match = re.match(datePattern, dateStr)
    if not match:
        print("Дата введена некорректно.")
        return

    year, month, day = map(int, match.groups())
    weekdayNumber = calendar.weekday(year, month, day)
    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(f"День недели: {weekdays[weekdayNumber]}")

findWeekdayOfDate()


def calculateFallTime():
    height = input("Введите высоту падения в метрах: ")
    try:
        height = float(height)
    except ValueError:
        print("Введите корректное числовое значение для высоты.")
        return

    if math.isnan(height):
        print("Высота должна быть числом.")
        return

    g = 9.8  # ускорение свободного падения, м/с^2
    fallTime = math.sqrt(2 * height / g)
    print(f"Время падения с высоты {height} метров составляет {fallTime:.2f} секунд.")

calculateFallTime()
