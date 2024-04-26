import re
def checkNumber(phoneNumber):
    pattern = r"^(00373|\+373|0)?[0-9]{8}$"

    if re.match(pattern, phoneNumber):
        return True
    else:
        return False

inputNumber = input("Введите номер телефона: ")

try:
    if checkNumber(inputNumber):
        print("Номер телефона корректен.")
    else:
        print("Номер телефона некорректен.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
