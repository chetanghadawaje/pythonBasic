"""
This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create
methods and specified objects.
"""


class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __int__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            return Singleton.__instance


s = Singleton()
print(id(s))

s1 = Singleton()
print(id(s1))
