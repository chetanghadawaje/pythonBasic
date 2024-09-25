"""
Two Sum problem: nums = [2, 7, 11, 15], target = 9, output = [0, 1]
"""

def two_sum(list1, target):
    for i in range(len(list1)-1):
        if list1[i] + list1[i+1] == target:
            return [i, i+1]
    return [None, None]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2, 7, 11, 15, 2, 3], 15))
print(two_sum([2, 7, 11, 15, 2, 3], 5))

"""
Output:
[0, 1]
[None, None]
[4, 5]
"""