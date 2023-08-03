# 216. Combination Sum III

# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def dfs(k, n, level, sol, result):
            if n < 0 or k < 0:
                return
            if n == 0 and k == 0:
                result.append(sol)
            for i in range(level, 10):
                dfs(k - 1, n - i, i + 1, sol + [i], result)
        dfs(k, n, 1, [], result)
        return result