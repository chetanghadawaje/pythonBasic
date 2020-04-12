"""
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
 mentioned in the sequence passed along.This function is defined in “functools” module.
"""

import functools


lis = [1, 3, 4, 10, 4]

print("The summation of list using reduce is :", end="")

print(functools.reduce(lambda x, y: x+y, lis))
