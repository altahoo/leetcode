# 485. Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        cur_max = 0
        for num in nums:
            if num:
                cur_max += 1
            elif cur_max:
                result = max(result, cur_max)
                cur_max = 0
        return max(result, cur_max)