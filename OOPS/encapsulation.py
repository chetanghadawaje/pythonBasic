"""
_ = Protected members [neither be accessed outside the class nor by any base class]
__ = Private members [which cannot be accessed outside the class but can be accessed from within the class and it’s
                     subclasses]
"""


class Person():
    def __init__(self, name=None, age=None):
        self._name = name
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, age, collage=None):
        Person.__init__(self, name=name, age=age)
        self.collage = collage


student_obj = Student("Chetan", 23, "SIBAR")

#print(student_obj.__age)
"""Out side class not access"""
print(student_obj.get_age())

student_obj._name = "Mahesh"
print(student_obj._name)

student_obj.collage = "CMCS"
print(student_obj.collage)