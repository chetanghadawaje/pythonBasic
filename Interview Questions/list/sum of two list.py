list1 = [1, 2, 3]
list2 = [9, 8, 7]


def sum1(i, j):
    return i + j


output3 = map(sum1, list1, list2)
print(list(output3))

"""
output:
[10, 10, 10]
"""