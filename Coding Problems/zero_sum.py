"""
Given an integer array, check if it contains a contiguous subarray having zero-sum.

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: True
Explanation: The subarrays with zero-sum are

[3, 4, -7]
[4, -7, 3]
[-7, 3, 1, 3]
[3, 1, -4]
[3, 1, 3, 1, -4, -2, -2]
[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

Input : [4, -7, 1, -2, -1]
Output: False
Explanation: The subarray with zero-sum doesn't exist.

"""
from typing import List


class Solution:
    def hasZeroSumSubarray(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                if sum(nums[i:j]) == 0:
                    return True
        return False
