from human import Human


class President(Human):
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