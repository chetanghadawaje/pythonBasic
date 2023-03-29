import old


def multi(value1, value2):
    return value1 * value2


print("Call sum function using 1,2 :", old.sum(1, 2))

print("Call multi function using 2,3 :", multi(2, 3))

# apply monkey patching
old.sum = multi

print("Call sum function using 2,3 :", old.sum(2, 3))
