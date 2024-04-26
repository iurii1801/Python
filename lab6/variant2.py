import re

class Employee:
    def __init__(self, name, phone, birthday, email, specialty):
        self.__name = name
        self.__phone = phone
        self.__birthday = birthday
        self.__email = email
        self.__specialty = specialty

    def calculateAge(self):
        # Реализация вычисления возраста
        pass

    def _calculateSalary(self):
        # Базовый класс не реализует расчет зарплаты
        return 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not re.match(r"^[A-Za-z]+$", value):
            raise ValueError("Имя должно содержать только буквы.")
        self.__name = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not re.match(r"^\+373\d{8}$", value):
            raise ValueError("Телефон должен соответствовать шаблону +373xxxxxxxx.")
        self.__phone = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if not re.match(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.(19[6-9][0-9]|200[0-7])$", value):
            raise ValueError("Дата рождения должна быть в формате ДД.ММ.ГГГГ от 1960 до 2007 года.")
        self.__birthday = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not re.match(r"^[A-Za-z0-9._-]{2,20}@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$", value):
            raise ValueError("Email должен быть действительным.")
        self.__email = value

    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self, value):
        if not re.match(r"^[A-Za-z]{4,20}$", value):
            raise ValueError("Специальность должна содержать от 4 до 20 букв.")
        self.__specialty = value

class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, hourlyRate, hoursWorked):
        super().__init__(name, phone, birthday, email, specialty)
        self.__hourlyRate = hourlyRate
        self.__hoursWorked = hoursWorked

    def _calculateSalary(self):
        return self.__hourlyRate * self.__hoursWorked

    @property
    def hourlyRate(self):
        return self.__hourlyRate

    @hourlyRate.setter
    def hourlyRate(self, value):
        if value < 0:
            raise ValueError("Почасовая ставка должна быть неотрицательной.")
        self.__hourlyRate = value

    @property
    def hoursWorked(self):
        return self.__hoursWorked

    @hoursWorked.setter
    def hoursWorked(self, value):
        if value < 0:
            raise ValueError("Количество отработанных часов должно быть неотрицательным.")
        self.__hoursWorked = value

class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, monthlySalary):
        super().__init__(name, phone, birthday, email, specialty)
        self.__monthlySalary = monthlySalary

    def _calculateSalary(self):
        return self.__monthlySalary

    @property
    def monthlySalary(self):
        return self.__monthlySalary

    @monthlySalary.setter
    def monthlySalary(self, value):
        if value < 0:
            raise ValueError("Месячная зарплата должна быть неотрицательной.")
        self.__monthlySalary = value
