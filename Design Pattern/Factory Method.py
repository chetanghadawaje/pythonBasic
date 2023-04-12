"""
Factory Method is a creational design pattern used to create concrete implementations of a common interface.
It separates the process of creating an object from the code that depends on the interface of the object.
"""


class AddTwoNumber(object):

    def calculation(self, a=0, b=0):
        return a + b


class MinsTwoNumber(object):

    def calculation(self, a=0, b=0):
        return a - b


def result(opertions="add"):
    """Factory Method"""
    localizers = {
        "add": AddTwoNumber,
        "mins": MinsTwoNumber,
    }
    # here add new class and call them same as above class.
    return localizers.get(opertions)


print(f'Call Add method: {result("add").calculation(2, 3)}')
print(f'Call Mins method: {result("mins").calculation(5, 2)}')
