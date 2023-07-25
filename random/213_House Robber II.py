# 213. House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        rob_first = [0] + [nums[0]] + [0] * (n - 1)
        not_rob_first = [0] * (n + 1)
        for i in range(2, n + 1):
            rob_first[i] = max(rob_first[i - 2] + nums[i - 1], rob_first[i - 1])
            not_rob_first[i] = max(not_rob_first[i - 2] + nums[i - 1], not_rob_first[i - 1])
        return max(rob_first[-2], not_rob_first[-1])