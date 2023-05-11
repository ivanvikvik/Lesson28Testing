class Super(object):
    def walk(self):
        print("I can walk.")


class Subclass(Super):
    pass


sup = Super()
sup.walk()
sub = Subclass()
sub.walk()
