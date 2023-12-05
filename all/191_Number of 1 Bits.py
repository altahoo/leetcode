# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += 1
            n &= (n - 1)  # flip the least significant bit to 0
        return result