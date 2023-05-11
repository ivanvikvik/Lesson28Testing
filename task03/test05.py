class Super(object):
    def walk(self):
        print("I can walk.")


class Subclass(Super):
    pass


base = Super()
sub = Subclass()

print(f"Is Subclass Super? - {issubclass(Subclass, Super)}")    # True
print(f"Is Super Subclass? - {issubclass(Super, Subclass)}")    # False
print(f"Is Super object? - {issubclass(Super, object)}")        # True
print(f"Is Subclass object? - {issubclass(Subclass, object)}")  # True

