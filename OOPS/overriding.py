class Animal(object):
    def voice(self):
        print("This is animal voice")


class Cat(Animal):
    def voice(self):
        print("Meow")


class Dog(Cat):
    def voice(self):
        print("Bho Bho")


class Cow(Dog):
    def voice(self):
        print("Hamba")


animal = Animal()
animal.voice()

