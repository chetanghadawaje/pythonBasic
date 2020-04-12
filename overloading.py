"""
python does not supports method overloading. We may overload the methods but can only use the latest defined method.
"""


def add(a=0, b=0, c=0):
    print(a + b + c)


add()
add(1)
add(1, 2)
add(1, 2, 3)