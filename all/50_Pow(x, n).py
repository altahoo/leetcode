# 50. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        
        result = 1

        while n:
            if n % 2 == 0:  # even
                x *= x
                n /= 2
            else:
                result *= x
                n -= 1
        return result