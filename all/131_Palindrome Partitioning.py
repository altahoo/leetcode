# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(str):
            return str == str[::-1]

        if not s:
            return [[]]
        
        result = []
        for i in range(len(s)):
            if not is_palindrome(s[:i + 1]):
                continue
            for palindromes in self.partition(s[i + 1:]):
                result.append([s[:i + 1]] + palindromes)
        return result