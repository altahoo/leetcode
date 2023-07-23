# 198. House Robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob_sum = [0] * (n + 2)
        for i in range(2, n + 2):
            rob_sum[i] = max(rob_sum[i - 1], rob_sum[i - 2] + nums[i - 2])
        return rob_sum[-1]
