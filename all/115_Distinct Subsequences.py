# 115. Distinct Subsequences

# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]: the number of dinstinct subsequences of s[:i] which equals t[:j]
        m, n = len(s), len(t) 
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] if s[i - 1] != t[j - 1] else dp[i - 1][j] + dp[i - 1][j - 1]

        return dp[m][n]