from human import Human


class Student(Human):
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