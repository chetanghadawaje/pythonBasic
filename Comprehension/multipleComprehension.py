temp = [(x, y) for x in range(5) for y in range(2)]

print(temp)

"""
Output:-
[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1)]
"""

nums = [1, 2, 3, 4, 5]
target = 7

left = 0
right = len(nums) - 1
result = []

while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        result.append([left, right])
        left += 1
        right -= 1
    elif current_sum < target:
        left += 1
    else:
        right -= 1

print(result)
