# Worker - Entity Class
class Worker:
    def __init__(self, name='no name', age='1', alive=True, salary=0):
        self.__name = name
        self.__age = age
        self.__alive = alive
        self.__salary = salary

    def can_work(self):
        print(self.__name + " can work.")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int) and salary > 0:
            self.__salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age=1):
        if 0 < age <= 120:
            self.__age = age

    @property
    def is_alive(self):
        return "Yes" if self.__alive else "No"

    @is_alive.setter
    def is_alive(self, alive):
        if isinstance(alive, bool):
            self.__alive = alive

    def __str__(self):
        return f"{self.__name}: age = {self.__age}. " \
               f"Is alive? - {self.is_alive}"
