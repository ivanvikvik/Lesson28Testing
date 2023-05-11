class Super(object):
    def __init__(self, name="Alex"):
        self._name = name

    # dynamic method
    def walk(self):
        print("I can walk.")

    @property
    def name(self):
        return self._name

    @staticmethod
    def smethod():
        print("static method from Super class")

    @classmethod
    def cmethod(cls):
        print("class method from Super class")

    def function(a, b):
        c = a + b
        print(c)

class Subclass(Super):
    pass


sub = Subclass("Peter Pen")
sub.walk()
print(sub._name)
print(sub.name)
Subclass.smethod()
sub.smethod()
Subclass.cmethod()
sub.cmethod()
Subclass.function(4, 5)
# sub.function(5, 6)    # TypeError
