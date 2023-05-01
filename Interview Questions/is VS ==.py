""" the difference between "is" and "==" operators"""

list_a = list()
list_b = list()
list_c = list_a

"""==: When the variables on either side have the exact same value, the == operator evaluation is true. Otherwise, it will evaluate as 
False."""
case_equal_1 = list_a == list_b
case_equal_2 = list_a == list_c
print(f"list_a == list_b: {case_equal_1}")
print(f"list_a == list_c: {case_equal_2}")


"""is: When the variables on either side of an operator point at the exact same object, the is operator’s evaluation is true. Otherwise, 
it will evaluate as False."""
case_is_1 = list_a is list_b
case_is_2 = list_a is list_c
print(f"list_a is list_b: {case_is_1}")
print(f"list_a is list_c: {case_is_2}")
