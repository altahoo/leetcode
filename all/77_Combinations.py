# 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def _dfs(num, cur_result):
            if len(cur_result) == k:
                result.append(cur_result.copy())
                return
            for i in range(num, n + 1):
                cur_result.append(i)
                _dfs(i + 1, cur_result)
                cur_result.remove(i)
        
        _dfs(1, [])
        return result