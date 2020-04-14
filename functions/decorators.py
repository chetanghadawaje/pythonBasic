def convert_upper(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.upper()
    return wrap


@convert_upper
def my_name(name):
    return name


print(my_name("chetan"))