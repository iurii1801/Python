import functions as func
def main():
    height = float(input("Введите ваш рост в см: "))
    age = int(input("Введите ваш возраст в годах: "))
    gender = input("Введите ваш пол (М/Ж): ").upper()

    ideal = func.idealWeight(height, age, gender)
    print(f"Ваш идеальный вес составляет: {ideal} кг.")

    actualWeight = float(input("Введите ваш текущий вес в кг: "))
    recommendation = func.weightRecommendation(actualWeight, ideal)
    print(recommendation)

main()
