class Super1(object):
    def walk(self):
        print("I can walk.")


class Super2(object):
    def run(self):
        print("I can run.")


class Subclass(Super1, Super2):
    pass

