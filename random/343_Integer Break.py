# 343. Integer Break

# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        
        # Greedily multiply all threes
        # When remainder = 1, we minus one 3 because (3+1) can be split into two 2s.
        threes = n // 3 - (n % 3 == 1)

        twos = 0 if not n % 3 else (2 if n % 3 == 1 else 1)
        return 3**threes * 2**twos

