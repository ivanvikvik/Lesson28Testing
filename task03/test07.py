class Super(object):
    def __init__(self, id=0):
        self.id = id

    def just_do_it(self):
        print("I'm working...")
        print("I'm working...")
        print("I'm working...")
        print("I'm working...")


class Subclass(Super):
    def __init__(self, id, name="no name"):
        super().__init__(id)
        self.name = name

    def just_do_it(self):
       super().just_do_it()
       print("I'm hard working...")


s = Subclass()
