def decorators_one(fun):
    def wrapper(*args, **kwargs):
        print("Decorator One")
        return fun(*args, **kwargs)
    return wrapper


def decorators_two(fun):
    def wrapper(*args, **kwargs):
        print("Decorator Two")
        return fun(*args, **kwargs)
    return wrapper


@decorators_one
@decorators_two
def test():
    print("Call test function")
    return "End Function"


if __name__ == '__main__':
    value = test()
    print(value)

"""
Output:
Decorator One
Decorator Two
Call test function
End Function
"""