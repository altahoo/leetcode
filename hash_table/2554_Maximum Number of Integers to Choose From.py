# 2554. Maximum Number of Integers to Choose From a Range I

# You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

# The chosen integers have to be in the range [1, n].
# Each integer can be chosen at most once.
# The chosen integers should not be in the array banned.
# The sum of the chosen integers should not exceed maxSum.
# Return the maximum number of integers you can choose following the mentioned rules.

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        buckets = [0] * n
        for number in banned:
            if 1 <= number <= n:
                buckets[number - 1] += 1
        
        result = 0
        idx = set()
        for i in range(n):
            if buckets[i] == 0:
                result += i + 1
                idx.add(i)
            if result > maxSum:
                return len(idx) - 1
        return len(idx)


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned) 
        total = 0
        numbers = set()
        for i in range(1, n + 1):
            if i not in banned:
                total += i
                numbers.add(i)
            if total > maxSum:
                return len(numbers) - 1
        return len(numbers)