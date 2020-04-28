"""
Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, but let
subclasses decide which class or object to instantiate.
"""
from abc import ABC, abstractmethod


class animal(metaclass=ABC):

    @abstractmethod
    def voice(self):
        pass



