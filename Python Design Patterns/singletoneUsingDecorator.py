def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class MyClass():
    def __init__(self, name):
        self.name = name


a = MyClass('abc')
b = MyClass('xyz')
print(f'{a.name=}')
print(f'{b.name=}')

print(a is b)