# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n % 2 != 0:
            return False
        
        while n:
            if n >> 1 and n & 1:
                return False
            n >>= 1
        
        return True