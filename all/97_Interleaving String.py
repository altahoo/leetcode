# 97. Interleaving String

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if (len1 + len2) != len3:
            return False
        
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]

        dp[0][0] = True
        for i in range(1, len1 + 1):
            dp[i][0] = s1[:i] == s3[:i]
        for j in range(1, len2 + 1):
            dp[0][j] = s2[:j] == s3[:j]
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])
        return dp[len1][len2]
