"""
A namespace is a collection of currently defined symbolic names along with information about the object that each 
name references.
There are four types of namespaces:
1) Built-In
2) Global
3) Local
"""


""" 
1) Built-In 
The built-in namespace contains the names of all of Python’s built-in objects.
"""
dir(__builtins__)


"""
2) Global
The global namespace contains any names defined at the level of the main program.
"""
a = 10

"""
3) Local
This namespace includes local names inside a function. This namespace is created when a function is called, and it only
lasts until the function returns.
"""


def local_name():
    a = 20
    print(f"A = {a}")


local_name()
print(f"A = {a}")

"""
output:
A = 20
A = 10
"""
