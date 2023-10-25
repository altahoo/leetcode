# 78. Subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def _dfs(idx, subset):
            result.append(subset.copy())

            for i in range(idx, len(nums)):
                subset.append(nums[i])
                _dfs(i + 1, subset)
                subset.pop()
        
        _dfs(0, [])
        return result