from human import Human


class Worker(Human):
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
