from human import Human


class Worker(Human):
    def __init__(self, name='no name', age='1', alive=True, salary=0):
        super().__init__(name, age, alive)
        self.__salary = salary

    def can_work(self):
        print(self.name + " can work.")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int) and salary > 0:
            self.__salary = salary

    def __str__(self):
        return (super().__str__()
                + f"Salary: {self.__salary}")