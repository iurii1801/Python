import datetime
def calculateAgeInDays():
    today = datetime.date.today()

    dateInput = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")

    try:
        year, month, day = map(int, dateInput.split('-'))
        birthDate = datetime.date(year, month, day)

        if birthDate > today:
            print("Дата рождения не может быть в будущем.")
            return

        lifeDays = today - birthDate
        print(f"Ваш возраст в днях - {lifeDays.days}")
    except ValueError as e:
        print(f"Некорректная дата. Убедитесь, что дата введена корректно и соответствует формату ГГГГ-ММ-ДД: {e}")


calculateAgeInDays()