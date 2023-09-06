# 525. Contiguous Array

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result, cur_sum = 0, 0
        n = len(nums)
        sum_to_first_end = {0: -1}

        for i in range(n):
            cur_sum += 1 if nums[i] == 1 else -1
            if cur_sum in sum_to_first_end:
                result = max(result, i - sum_to_first_end[cur_sum])
            else:
                sum_to_first_end[cur_sum] = i
        
        return result
