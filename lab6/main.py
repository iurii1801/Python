# Импорт из одного из вариантов модулей:
from variant1 import Employee, HourlyEmployee, SalaryEmployee
# from variant2 import Employee, HourlyEmployee, SalaryEmployee

def createEmployee(cls, employeeType):
    print(f"\nСоздание сотрудника типа {employeeType}:")
    name = input("Введите имя: ")
    phone = input("Введите телефон (+373xxxxxxxx): ")
    birthday = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
    email = input("Введите email: ")
    specialty = input("Введите специальность: ")
    if cls is HourlyEmployee:
        hourlyRate = float(input("Введите почасовую ставку: "))
        hoursWorked = float(input("Введите количество отработанных часов: "))
        return cls(name, phone, birthday, email, specialty, hourlyRate, hoursWorked)
    elif cls is SalaryEmployee:
        monthlySalary = float(input("Введите месячную зарплату: "))
        return cls(name, phone, birthday, email, specialty, monthlySalary)
    else:
        return cls(name, phone, birthday, email, specialty)

def inputEmployees():
    generalEmployee = createEmployee(Employee, "обычный")
    hourlyEmployee = createEmployee(HourlyEmployee, "почасовой")
    salaryEmployee = createEmployee(SalaryEmployee, "с фиксированной оплатой")
    return generalEmployee, hourlyEmployee, salaryEmployee

def displaySalaries(*employees):
    print("\nЗарплаты всех сотрудников:")
    for employee in employees:
        salary = employee._calculateSalary()
        if salary is not None:
            print(f"{employee.name}: {salary} леев.")
        else:
            print(f"{employee.name}: Нет зарплаты (неприменимо)")

# Сбор данных о всех сотрудниках
generalEmployee, hourlyEmployee, salaryEmployee = inputEmployees()

# Отображение зарплат всех сотрудников
displaySalaries(generalEmployee, hourlyEmployee, salaryEmployee)

