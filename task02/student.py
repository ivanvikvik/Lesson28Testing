from human import Human


class Student(Human):
    def __init__(self, name='no name', age='1', alive=True, mark=4):
        super().__init__(name, age, alive)
        self.__mark = mark

    def can_study(self):
        print(self.name + " can study.")

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if 0 <= mark <= 10:
            self.__mark = mark

    def __str__(self):
        return (super().__str__()
                + f"Mark: {self.__mark}")