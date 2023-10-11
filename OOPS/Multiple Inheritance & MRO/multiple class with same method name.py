"""
where we have class C derived from both A and B. When method process() is called with object of class C then process() method
Class A     Class B
    |          |
    ------------
          |
       Class C
"""


class A:
    def process(self):
        print("Process A")


class B:
    def process(self):
        print("Process B")


class C(A, B):
    pass


obj_c = C()
obj_c.process()

"""
Output:
Process A
"""