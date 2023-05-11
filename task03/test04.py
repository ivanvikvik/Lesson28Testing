class Super(object):
    def walk(self):
        print("I can walk.")


class Subclass(Super):
    pass


base = Super()
sub = Subclass()

print(f"Is base Super? - {isinstance(base, Super)}")        # True
print(f"Is base Subclass? - {isinstance(base, Subclass)}")  # False
print(f"Is sub Super? - {isinstance(sub, Super)}")          # True
print(f"Is sub Subclass? - {isinstance(sub, Subclass)}")    # True
