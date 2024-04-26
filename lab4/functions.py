def idealWeight(height, age, gender):
    if gender == 'М':
        idealWeight = height - 100 - ((height - 150) / 4 + (age - 20) / 4)
    elif gender == 'Ж':
        idealWeight = height - 100 - ((height - 150) / 2.5 + (age - 20) / 6)
    else:
        return "Ошибка: Некорректно указан пол. Введите 'М' или 'Ж'."
    return idealWeight

def weightRecommendation(actualWeight, idealWeight):
    if actualWeight < idealWeight:
        return "Рекомендуется набрать вес."
    elif actualWeight > idealWeight:
        return "Рекомендуется снизить вес."
    else:
        return "Ваш вес идеален!"
