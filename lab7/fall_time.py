import math
def calculateFallTime():
    try:
        height = float(input("Введите высоту падения в метрах: "))
        if height < 0:
            print("Высота не может быть отрицательной.")
            return
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числовое значение высоты.")
        return

    g = 9.8  # ускорение свободного падения в м/с²
    time = math.sqrt(2 * height / g)
    print(f"Время падения с высоты {height} метров составляет {time:.2f} секунд.")

calculateFallTime()
