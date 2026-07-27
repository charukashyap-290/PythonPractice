
class Animal:
    def sound(self):
        print("Animals make different sounds")


class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof")


class Cow(Animal):
    def sound(self):
        print("Cow moos: Moo Moo")


d = Dog()
c = Cow()


# d.sound()
# c.sound()