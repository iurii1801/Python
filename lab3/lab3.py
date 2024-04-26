# Задание 1.
# Проанализируйте следующие коды Python и потом объясните какие будут результаты их интерпретирования.

i = sum = 0
while i <= 0:
    sum += i
    i = i+1
print(sum)

# Инициализируются переменные i и sum равными 0, затем запускается цикл while,
# который будет выполняться, пока i меньше или равно 4.
# В каждой итерации цикла значение sum увеличивается на i, а затем i увеличивается на 1.
# По завершении цикла выводится значение sum. В результате будет выведено число 10.

for char in 'PYTHON STRING':
  if char == ' ':
      break
  print(char, end='')
  if char == 'O':
      continue
  print('*', end='')

# Используется цикл for для перебора каждого символа в строке 'PYTHON STRING'.
# Если символ равен пробелу, то цикл завершается с помощью оператора break.
# В противном случае символ выводится, а затем проверяется, равен ли он 'O'.
# Если да, выполняется оператор continue, который пропускает оставшийся код внутри цикла и переходит к следующей итерации.
# В противном случае после вывода символа '*' выводится символ '*', за которым следует окончание строки.
# В результате код выведет "P*Y*T*H*ON".




# Задание 2.
# Напишите код, который обрабатывает значение, введенное пользователем,
# и выводит какое-то сообщение ему, используя оператор if...elif...else.

# Ввод возраста
money = int(input("\n" "Введите вашу сумму: "))
if money < 5000:
  print("Вы студент.")
elif money >= 5000 and money < 15000:
  print("Вы среднестатистический работник.")
else:
  print("Вы программист.")



myList = [18, 76, 18, 20, 32, 18, 85, 18, 78, 32, 20, 32, 45.6]
myDict = {"speciality": "Informatica",
           "Lesson": "Python",
           "name": "Iura",
           "date": "18"
           }

# Счетчик для списка
countList = {}
# Проходимся по значениям
for element in myList:
  # Если значение еще не встречалось в countList, добавляем его как ключ и устанавливаем счетчик на 0
  if element not in countList:
    countList[element] = 0
    # Увеличиваем счетчик для данного значения
  countList[element] += 1

print("Количесво вхождений в списоке:")
for element, count in countList.items():
  print(f"{element}: {count}")


# Счетчик для словаря
countDict = {}
# Проходимся по значениям
for value in myDict.values():
    # Если значение еще не встречалось в countDict, добавляем его как ключ и устанавливаем счетчик на 0
    if value not in countDict:
        countDict[value] = 0
    # Увеличиваем счетчик для данного значения
    countDict[value] += 1

print("Количесво вхождений в словаре:")
for value, count in countDict.items():
  print(value + ": " + str(count))


summ = lambda x,y: x+y
print(summ(18,232))





# Задание 3. Создание списка покупок (shopping list)

import functions1 as func # псевдоним

# Список товаров
products = []

# Цикл меню
while True:
  print("\nМеню управления")
  print("1. Просмотреть список")
  print("2. Добавить товар")
  print("3. Удалить товар")
  print("4. Выход")

  choice = input("Выберите опцию: ")

  if choice == "1":
    func.showProducts(products)
  elif choice == "2":
    products = func.addProduct(products)
  elif choice == "3":
    products = func.removeProduct(products)
  elif choice == "4":
    print("До свидания!")
    break
  else:
    print("Вы выбрали несуществующую опцию! Выберите из существующих.")






