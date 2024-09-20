"""
unit test case using pytest module

This code need to pytest module installed
"""

from math_operations import multiple, divide

def test_multiply():
    assert multiple(2,2) == 4
    assert multiple(2,-2) == 4


def test_divide():
    assert divide(2,2) == 0
    assert divide(4,2)  == 1