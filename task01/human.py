# Human - Entity Class
class Human:

    def __init__(self, name='no name', age='1', alive=True):
        self.name = name
        self.age = age
        self.alive = alive

    def __str__(self):
        return (f"{self.name}: age = {self.age}. "
                f"Is alive? - {'YES' if self.alive else 'NO'}")


def main():
    h1 = Human()
    h1.name = 1234
    h1.age = -20
    print(h1)

    h2 = Human("Kate", 18, False)
    print(h2)


if __name__ == "__main__":
    main()
