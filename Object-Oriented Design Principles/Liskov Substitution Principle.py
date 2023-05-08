"""
Subtypes must be substitutable for their base types.

For example, if you have a piece of code that works with a Shape class, then you should be able to substitute that class with any of its
subclasses, such as Circle or Rectangle, without breaking the code.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


"""With this implementation in place, you can use the Shape type interchangeably with its Square and Rectangle subtypes when you only care 
about their common behavior"""


def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)


return_value = get_total_area([Rectangle(10, 5), Square(5)])
print(f"return_value: {return_value}")
# O/P: return_value: 75
