# 254. Factor Combinations

# Numbers can be regarded as the product of their factors.

# For example, 8 = 2 x 2 x 2 = 2 x 4.
# Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

# Note that the factors should be in the range [2, n - 1].

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []

        def helper(n, start, sol):
            if sol:
                result.append(sol + [n])
            
            for i in range(start, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    helper(n // i, i, sol + [i])
        
        helper(n, 2, [])
        return result