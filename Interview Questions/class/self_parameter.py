"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def my_func(abc):
        print(f"Hello my name is {abc.name}")

    def my_age(self):
        print(f"Hello my age is {self.age}")


p1 = Person("John", 36)
p1.my_func()
p1.my_age()
