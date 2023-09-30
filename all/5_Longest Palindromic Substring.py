# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

class Solution:

    def longestPalindrome(self, s: str) -> str:
        def _palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        result = ''
        for i in range(len(s)):
            palindrome = _palindrome(i, i + 1)
            if len(palindrome) > len(result):
                result = palindrome
            palindrome = _palindrome(i - 1, i + 1)
            if len(palindrome) > len(result):
                result = palindrome
            
        return result