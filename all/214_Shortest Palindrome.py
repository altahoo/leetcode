# 214. Shortest Palindrome

# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.


# TLE
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def is_palindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1
            return True
        
        if s == s[::-1]:
            return s

        for end in range(len(s), 0, -1):
            if is_palindrome(s[:end]):
                return s[end:][::-1] + s
        
        return s[1:][::-1] + s


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s + '#' + s[::-1]
        dp = [0] * len(t)
        for i in range(1, len(t)):
            j = dp[i - 1]
            while j and t[i] != t[j]:
                j = dp[j - 1]
            dp[i] = j + 1 if t[i] == t[j] else j
        return s[::-1][:len(s) - dp[-1]] + s