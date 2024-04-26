#  Добавление нового товара в список
def addProduct(products):

  product = input("Введите название товара: ")
  products.append(product)
  return products


#  Удаление товара из списка
def removeProduct(products):

  while True:
    try:
      # Выбор способа удаления
      choice = input("Способ удаления по порядковому номеру (1) или названию (2)? ")
      if choice not in ("1", "2"):
        raise ValueError # Возбуждаем исключение, если выбор не является корректным

      # Удаление по порядковому номеру
      if choice == "1":
        index = int(input("Введите порядковый номер товара: "))
        # Корректировка индекса на 1, чтобы соответствовать индексации списка
        index -= 1
        # Проверка корректности индекса
        if not 0 <= index < len(products): # Убеждаемся, что index больше или равен 0 и
                                           # что index меньше, чем количество элементов в списке products

          raise IndexError  # Возбуждаем исключение, если номер товара вне диапазона

        del products[index]
        print(f"Товар под номером {index + 1} удален")
        break # Прерываем цикл while, так как удаление товара выполнено успешно

      # Удаление по названию
      elif choice == "2":
        product = input("Введите название товара: ")
        if product not in products:
          raise ValueError  # Возбуждаем исключение, если товар не найден в списке

        products.remove(product)
        print(f"Товар '{product}' удален")
        break # Прерываем цикл while, так как удаление товара выполнено успешно
    except (ValueError, IndexError):
      print("Неверный ввод. Попробуйте снова.")

  return products



# Отображение списка товаров
def showProducts(products):

  # Перебор списка товаров с нумерацией, начиная с 1
  for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")



