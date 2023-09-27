"""
When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the
base case.
"""


class Person:
    def __init__(self):
        super().__init__()
        print("This is a Person class.")

    def display(self):
        print("Person class display method.")


class Address:
    def __init__(self):
        print("This is an Address class.")

    def display(self):
        print("Address class display method.")


class Student(Person, Address):
    def __init__(self):
        super().__init__()
        # Person()
        print("This is a Student class.")


student_obj = Student()
print("Student MRO: ", Student.__mro__)
