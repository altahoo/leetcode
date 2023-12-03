# 190. Reverse Bits

# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        result, power = 0, 31
        while n:
            result += (n & 1) << power
            n >>= 1
            power -= 1
        return result