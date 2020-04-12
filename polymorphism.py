"""
same function name (but different signatures) being uses for different types
"""

print("""
Polymorphism with Inheritance
""")


class Country:
    def type(self):
        print("This is country info:")


class India(Country):
    def info(self):
        print("This is India")


class USA(Country):
    def info(self):
        print("This is USA")


obj_in = India()
obj_usa = USA()

obj_in.type()
obj_in.info()

obj_usa.type()
obj_usa.info()


print("""
Polymorphism with a Function and objects
""")


class India():
    def info(self):
        print("This is India")


class USA():
    def info(self):
        print("This is USA")


def func(obj):
    obj.info()


obj_in = India()
obj_usa = USA()

func(obj_in)
func(obj_usa)