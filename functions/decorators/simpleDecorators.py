def simple_decorators(fun):
    def wrapper(*args, **kwargs):
        print("Step 1")
        fun(*args, **kwargs)
        print("Step 2")
    return wrapper


@simple_decorators
def simple_function():
    print("Test")


simple_function()


"""
Output:
Step 1
Test
Step 2
"""