# Human - Entity Class
class Human:

    def __init__(self, name='no name', age='1', alive=True):
        self.__name = name
        self.__age = age
        self.__alive = alive

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and 0 < age <= 120:
            self.__age = age

    def is_alive(self):
        return self.__alive

    def set_alive(self, alive):
        if isinstance(alive, bool):
            self.__alive = alive

    def __str__(self):
        return f"{self.__name}: age = {self.__age}. " \
               f"Is alive? - {'YES' if self.__alive else 'NO'}"


def main():
    h1 = Human()
    h1.set_name(1234)
    h1.set_age(-20)
    print(h1)

    h2 = Human("Kate", 18, False)
    print(h2)


if __name__ == "__main__":
    main()
