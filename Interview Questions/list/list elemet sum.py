"""
list element sum i/p = [1,2,3,4,5,6] target sum = 6 output = [[1,2,3],[1,5]]
"""

from itertools import combinations

def find_subsets(nums, target):
    result = []
    # Check combinations of all lengths from 1 to the length of the list
    for r in range(1, len(nums) + 1):
        # Generate all combinations of the current length r
        for subset in combinations(nums, r):
            # If the sum of the subset matches the target, add it to the result
            if sum(subset) == target:
                result.append(list(subset))
    return result


# Input list and target sum
input_list = [1, 2, 3, 4, 5, 6]
target_sum = 6
# Finding subsets
output = find_subsets(input_list, target_sum)
print(output)