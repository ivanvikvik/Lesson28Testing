# Student - Entity Class
class Student:
    def __init__(self, name='no name', age='1', alive=True, mark=4):
        self.__name = name
        self.__age = age
        self.__alive = alive
        self.__mark = mark

    def can_study(self):
        print(self.__name + " can study.")

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if 0 <= mark <= 10:
            self.__mark = mark

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
        return f"{self.__name}: age = {self.__age}, " \
               f"mark = {self.__mark}. " \
               f"Is alive? - {self.is_alive}"
