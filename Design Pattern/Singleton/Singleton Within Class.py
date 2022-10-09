"""
This pattern restricts the instantiation of a class to one object. It is a type of creation pattern and involves only one class to create
methods and specified objects.

DISADVANTAGE: Using new method every time __init__() method call.
"""


class Singleton:
    __instance = None
    name = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


s2 = Singleton()
print(id(s2))

s = Singleton()
s.set_name("ABC")
s.get_name()
print(id(s))

s1 = Singleton()
print(id(s1))
s1.get_name()
