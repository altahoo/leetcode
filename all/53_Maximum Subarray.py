# 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_until_now = 0
        max_sum = -float('inf')
        for num in nums:
            if max_until_now >= 0:
                max_until_now += num
            else:
                max_until_now = num
            max_sum = max(max_sum, max_until_now)
        
        return max_sum