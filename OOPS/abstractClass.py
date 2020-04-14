from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print("Meow")


class Dog(Animal):
    def voice(self):
        print("bho")

    def speed(self):
        print("5km/hr")


obj_cat = Cat()
obj_cat.voice()

obj_dog = Dog()
obj_dog.speed()
obj_dog.voice()
