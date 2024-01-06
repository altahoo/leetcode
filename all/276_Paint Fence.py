# 276. Paint Fence

# You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

# Every post must be painted exactly one color.
# There cannot be three or more consecutive posts with the same color.
# Given the two integers n and k, return the number of ways you can paint the fence.

class Solution:
    def numWays(self, n: int, k: int) -> int:

        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            
            if i in memo:
                return memo[i]
            
            memo[i] = (k - 1) * (total_ways(i - 1) + total_ways(i - 2))
            return memo[i]
        memo = {}
        return total_ways(n)