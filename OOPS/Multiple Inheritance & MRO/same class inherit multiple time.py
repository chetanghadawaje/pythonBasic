"""
MRO owing to complexity of hierarchy. In such cases it will throw an error as demonstrated by the following code
        Class A ----
            |       |
            |    Class B
            |       |
        Class C  ---
"""


class A:
    def process(self):
        print("Process A")


class B(A):
    def process(self):
        print("Process B")


class C(A, B):
    pass


obj = C
obj.process()

"""
output:
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B
"""