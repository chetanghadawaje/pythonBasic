def string_operation(fun):
    def wrapper(*args, **kwargs):
        x = args[0]
        x = x.upper()
        print("decorators variable value {0}".format(x))
        return fun(x)
    return wrapper


@string_operation
def print_name(name):
    print(f"Thank You!! {name}")
    print(name)
    return name


print_name("Chetan")
