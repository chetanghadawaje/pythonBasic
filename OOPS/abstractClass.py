"""
An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within
any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An
abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we
use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.
"""

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
