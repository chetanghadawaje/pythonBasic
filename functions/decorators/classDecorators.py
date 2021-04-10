class MyDecorators:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print("Class decorators call.")
        self.fun(*args, **kwargs)


@MyDecorators
def test():
    print("Test function call.")


test()

"""
Output:
Class decorators call.
Test function call.
"""