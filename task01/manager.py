from human import Human


# Manager - Function Class
class Manager:
    @staticmethod
    def count_adult(humans):
        if isinstance(humans, (list, tuple)):
            count = 0

            for human in humans:
                if isinstance(human, Human) and human.age >= 18:
                    count += 1

            return count

    @staticmethod
    def count_underage(humans):
        total = len(humans)
        total -= Manager.count_adult(humans)
        return total
