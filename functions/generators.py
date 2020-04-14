"""
A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
"""


# Ex1
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)


# Ex2
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


print(list(PowTwoGen(10)))