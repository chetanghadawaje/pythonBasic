my_list = [23, 45, 54, 1, 65, 98, 76, 9, 12, 11, 345, 99]
my_list.sort()


def BinarySearch(s_list, high, low, fun_target):
    if high >= low:
        mid = (high+low) // 2
        if s_list[mid] == fun_target:
            return mid

        if s_list[mid] < fun_target:
            """If the midpoint value is less than the target value, the function recursively calls itself with the new search range defined
             by the midpoint index plus one and the current highest index."""
            return BinarySearch(s_list, high, mid + 1, fun_target)
        else:
            """If the midpoint value is greater than the target value, the function recursively calls itself with the new search range 
            defined by the current lowest index and the midpoint index minus one."""
            return BinarySearch(s_list, mid - 1, low, fun_target)
    else:
        return None


target = 12
x = BinarySearch(my_list, len(my_list) - 1, 0, target)
if x is not None:
    print(f"{my_list} index of {target} is {x}")
else:
    print(f"{target} not found.")
