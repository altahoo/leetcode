# 172. Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        power_of_five = 5
        while n >= power_of_five:
            result += n // power_of_five
            power_of_five *= 5
        return result