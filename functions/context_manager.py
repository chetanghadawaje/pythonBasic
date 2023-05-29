"""
 When creating context managers using classes, user need to ensure that the class has the methods: __enter__() and __exit__(). The
 __enter__() returns the resource that needs to be managed and the __exit__() does not return anything but performs the cleanup operations.
"""


class ContextMangerExample(object):
    def __init__(self):
        print("This is INIT method.")

    def __enter__(self):
        print("This is ENTER method.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("This is EXIT method.")


with ContextMangerExample() as manger:
    print("In WITH keyword.")

"""
O/P: This is INIT method.
This is ENTER method.
In WITH keyword.
This is EXIT method.
"""