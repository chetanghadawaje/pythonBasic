""""""


# Create custom meta class
class MyMeta(type):
    pass


class MyClass(metaclass=MyMeta):
    pass
