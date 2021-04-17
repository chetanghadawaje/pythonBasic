"""
Q) Calling parent class __init__ with multiple inheritance
"""


class ClassA(object):

    def __init__(self):
        print("This is class A.")


class ClassB(ClassA):

    def __init__(self):
        print("Enter class B.")
        super(ClassB, self).__init__()
        print("This is class B.")


ClassB()
