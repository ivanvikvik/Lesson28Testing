from human import Human


# Manager - Function Class
class Manager:
    def count_adult(self, humans):
        if isinstance(humans, (list, tuple)):
            count = 0

            for human in humans:
                if (isinstance(human, Human)
                        and human.age >= 18):
                    count += 1

            return count

    def count_underage(self, humans):
        if isinstance(humans, (list, tuple)):
            total = len(humans)
            total -= self.count_adult(humans)
            return total


def main():
    h1 = Human("Alex", 20, 10)
    h2 = Human("Kate", 18, 7)
    h3 = Human("Garry", 15, 9)

    ls = (h1, h2, h3)

    mngr = Manager()
    underage = mngr.count_underage(ls)
    print(f"Underage people - {underage}")


if __name__ == "__main__":
    main()
