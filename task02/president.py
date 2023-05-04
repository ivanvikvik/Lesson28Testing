# Human - Entity Class
class President:
    def __init__(self, name='no name', age='1', alive=True, power=50):
        self.__name = name
        self.__age = age
        self.__alive = alive
        self.__power = power

    def can_run(self):
        print(self.__name + " can run.")

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        if isinstance(power, int) and 0 < power <= 100:
            self.__power = power

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
