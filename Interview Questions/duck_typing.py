"""if it walks like a duck, and it quacks like a duck, then it is probably be a duck."""


class Duck:
    def quack(self):
        print("I am a duck and I quack.")


class Goose:
    def quack(self):
        print("I am a goose and I quack.")


class Cat:
    def meow(self):
        print("I am a dog and I meow.")


def quack(animal):
    animal.quack()


quack(Duck())
quack(Goose())
quack(Cat())    # Here not support duck type.

"""
O/P: I am a duck and I quack.
I am a goose and I quack.
AttributeError: 'Cat' object has no attribute 'quack'
"""