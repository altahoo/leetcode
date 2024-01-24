# 312. Burst Balloons

# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for left in range(n-2, 0, -1):
            for right in range(left, n-1):
                for i in range(left, right + 1):
                    gain = nums[left - 1] * nums[i] * nums[right + 1]
                    remaining = dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(remaining + gain, dp[left][right])
        return dp[1][n-2]