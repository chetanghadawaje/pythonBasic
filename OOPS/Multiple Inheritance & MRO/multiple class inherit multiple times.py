"""
we create D from C and B. Classes C and B have process() method and as expected MRO chooses method from C. Remember it goes from left to
right. So it searches C first and all its super classes of C and then B and all its super classes.

Class A             Class B
    |                  | |
    -------  ----------  |
           |             |
        Class C          |
           |             |
           --------------
                  |
                Class D
"""


class A:
    def process(self):
        print("Process A")


class B:
    def process(self):
        print("Process B")


class C(A, B):
    def process(self):
        print("Process C")


class D(C, B):
    pass


obj = D()
print(D.mro())
obj.process()

"""
output:

"""
