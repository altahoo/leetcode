# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        n = len(nums)
        min_size = float(inf)
        curr_sum = 0
        while end < n:
            curr_sum += nums[end]
            while curr_sum >= target:
                min_size = min(min_size, end - start + 1)
                curr_sum -= nums[start]
                start += 1
            end += 1
        return min_size if min_size != float(inf) else 0
