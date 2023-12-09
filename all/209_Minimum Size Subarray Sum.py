# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, i  = 0, 0
        total = 0
        min_length = len(nums) + 1
        while i < len(nums):
            total += nums[i]
            while total >= target:
                min_length = min(min_length, i - start + 1)
                total -= nums[start]
                start += 1
            i += 1
        return min_length if min_length != len(nums) + 1 else 0
