def my_decorators(name):
    def repeat(fun):
        def wrapper(*args, **kwargs):
            if type(name) is str:
                print("{} is String".format(name))
            else:
                print("{} is not string".format(name))
            return fun(*args, **kwargs)
        return wrapper
    return repeat


@my_decorators(name="chetan")
def test():
    print("This is test function.")


if __name__ == '__main__':
    print("Test function call.")
    test()
