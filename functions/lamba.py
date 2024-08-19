"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""

min_value = lambda x, y: y if x > y else x

multi = lambda x, y: x * y

result = min_value(10, 20)
print(f"Min value of 10, 20 is {result}")

result_multi = multi(10, 20)
print(f"Multiplication of 10, 20 is {result_multi}")

"""
Output:
Min value of 10, 20 is 10
Multiplication of 10, 20 is 200
"""
