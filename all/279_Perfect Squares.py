# 279. Perfect Squares

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

class Solution:
    def numSquares(self, n: int) -> int:

        def is_divided_by(n, count):
            if count == 1:
                return n in square_nums
            
            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])
        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count