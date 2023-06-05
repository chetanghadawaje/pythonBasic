'''

Given an unsorted integer array, find a pair with the given sum in it.

• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()

'''
from typing import List, Tuple


class Solution:
    def findPair(self, nums: List[int], target: int) -> Tuple:
        for index, value in enumerate(nums):
            for i in range(index+1, len(nums)):
                if target == value + nums[i]:
                    return (value, nums[i])
        return ()


obj = Solution()
Input = [80, 70, 20, 60]
Target = 140
output = obj.findPair(Input, Target)
print(output)
