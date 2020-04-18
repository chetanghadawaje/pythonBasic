"""A] adding / after x, you specify that x is a positional-only argument"""


def add(a, /, b=0):
    print(a + b)

# add(a=10, 20)
# add(a=10, b=20)
add(10, b=20)


"""B] keyword-only arguments using the star (*). Any argument after * must be specified using a keyword"""


def add3(a, b, *, c):
    print(a + b + c)

add3(a=10, b=20, c=30)
# add3(10, 20, 10)
add3(20, 30, c=40)