import re

class Employee:
    def __init__(self, name, phone, birthday, email, specialty):
        self.__name = name
        self.__phone = phone
        self.__birthday = birthday
        self.__email = email
        self.__specialty = specialty

    def calculateAge(self):
        # Реализация вычисления возраста на основе даты рождения
        pass

    def _calculateSalary(self):
        # Базовый класс не реализует расчет зарплаты
        return 0

    def getName(self):
        return self.__name

    def setName(self, value):
        if not re.match(r"^[A-Za-z]+$", value):
            raise ValueError("Имя должно содержать только буквы.")
        self.__name = value

    name = property(getName, setName)

    def getPhone(self):
        return self.__phone

    def setPhone(self, value):
        if not re.match(r"^\+373\d{8}$", value):
            raise ValueError("Телефон должен соответствовать шаблону +373xxxxxxxx.")
        self.__phone = value

    phone = property(getPhone, setPhone)

    def getBirthday(self):
        return self.__birthday

    def setBirthday(self, value):
        if not re.match(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.(19[6-9][0-9]|200[0-7])$", value):
            raise ValueError("Дата рождения должна быть в формате ДД.ММ.ГГГГ от 1960 до 2007 года.")
        self.__birthday = value

    birthday = property(getBirthday, setBirthday)

    def getEmail(self):
        return self.__email

    def setEmail(self, value):
        if not re.match(r"^[A-Za-z0-9._-]{2,20}@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$", value):
            raise ValueError("Email должен быть действительным.")
        self.__email = value

    email = property(getEmail, setEmail)

    def getSpecialty(self):
        return self.__specialty

    def setSpecialty(self, value):
        if not re.match(r"^[A-Za-z]{4,20}$", value):
            raise ValueError("Специальность должна содержать от 4 до 20 букв.")
        self.__specialty = value

    specialty = property(getSpecialty, setSpecialty)

class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, hourlyRate, hoursWorked):
        super().__init__(name, phone, birthday, email, specialty)
        self.__hourlyRate = hourlyRate
        self.__hoursWorked = hoursWorked

    def _calculateSalary(self):
        return self.__hourlyRate * self.__hoursWorked

    def getHourlyRate(self):
        return self.__hourlyRate

    def setHourlyRate(self, value):
        if value < 0:
            raise ValueError("Почасовая ставка должна быть неотрицательной.")
        self.__hourlyRate = value

    hourlyRate = property(getHourlyRate, setHourlyRate)

    def getHoursWorked(self):
        return self.__hoursWorked

    def setHoursWorked(self, value):
        if value < 0:
            raise ValueError("Количество отработанных часов должно быть неотрицательным.")
        self.__hoursWorked = value

    hoursWorked = property(getHoursWorked, setHoursWorked)

class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, monthlySalary):
        super().__init__(name, phone, birthday, email, specialty)
        self.__monthlySalary = monthlySalary

    def _calculateSalary(self):
        return self.__monthlySalary

    def getMonthlySalary(self):
        return self.__monthlySalary

    def setMonthlySalary(self, value):
        if value < 0:
            raise ValueError("Месячная зарплата должна быть неотрицательной.")
        self.__monthlySalary = value

    monthlySalary = property(getMonthlySalary, setMonthlySalary)
