"""
i/p = “I play cricket” o/p = t play crickeI
"""

input_string = "I play cricket"
list_string = list(input_string)
list_string[0], list_string[-1] = list_string[-1], list_string[0]
print("".join(list_string))

"""
Output:
t play crickeI
"""