# 132. Palindrome Partitioning II

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.


class Solution:
    def minCut(self, s: str) -> int:

        def is_palindrome(str):
            return str == str[::-1]
        
        result = []
        for i in range(len(s)):
            if is_palindrome(s[:i + 1]):
                result.append(0)
            else:
                result.append(len(s) - 1)
                for j in range(i):
                    if is_palindrome(s[j + 1: i + 1]) and result[-1] > result[j] + 1:
                        result[-1] = result[j] + 1
        return result[-1]