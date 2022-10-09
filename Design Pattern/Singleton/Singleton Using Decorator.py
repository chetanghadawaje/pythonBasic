"""
Using decorator we handle singleton.
"""


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class SingletonClass:

    def __init__(self, name):
        print("Call __init__")
        self.name = name

    def get_name(self):
        print(f"Name: {self.name}")


s1 = SingletonClass("ABC")
s2 = SingletonClass("XYZ")

s1.get_name()
s2.get_name()
