# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        result = 0
        if s[0] == '-':
            result = -int(''.join(s[1:][::-1]))
        else:
            result = int(''.join(s[::-1]))
        
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result