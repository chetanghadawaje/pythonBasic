"""
Singleton class create using metaclass.
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):

    def __init__(self, name):
        print("Call __init__")
        self.name = name

    def get_name(self):
        print(f"Name: {self.name}")


s1 = SingletonClass("ABC")
s2 = SingletonClass("XYZ")

s1.get_name()
s2.get_name()