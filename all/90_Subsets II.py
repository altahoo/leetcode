# 90. Subsets II

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def _dfs(idx, subset):
            result.append(subset.copy())
            i = idx
            while i < len(nums):
                subset.append(nums[i])
                _dfs(i + 1, subset)
                subset.pop()
                i += 1
                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
        
        _dfs(0, [])
        return result