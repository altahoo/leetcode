325. Maximum Size Subarray Sum Equals k

# Given an integer array nums and an integer k, return the maximum length of a 
# subarray that sums to k. If there is not one, return 0 instead.

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum_idx = {}
        presum = 0
        result = 0
        for i, num in enumerate(nums):
            presum += num
            if presum == k:
                result = i + 1
            if presum - k in presum_idx:
                result = max(result, i - presum_idx[presum - k])
            if presum not in presum_idx:
                presum_idx[presum] = i
        return result