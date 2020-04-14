"""
[:=] that assigns values to variables as part of a larger expression
"""

l = (1, 2, 3, 4, 5, 6)

if (n := len(l)) > 4:
    print(n)
