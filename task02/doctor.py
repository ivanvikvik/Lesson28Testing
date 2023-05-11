from human import Human


class Doctor(Human):
    def __init__(self, name='no name', age='1', alive=True, experience=1):
        super().__init__(name, age, alive)
        self.__experience = experience

    def can_cure(self):
        print(self.name + " can cure.")

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, experience):
        if isinstance(experience, int) and experience > 0:
            self.__experience = experience

    def __str__(self):
        return (super().__str__()
                + f"Experience: {self.__experience}")
