# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True