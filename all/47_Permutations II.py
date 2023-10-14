# 47. Permutations II

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        def _has_duplicate(start, i, nums):
            for j in range(start, i):
                if nums[j] == nums[i]:
                    return True
            return False

        def _permute(start):
            if start == n - 1:
                result.append(nums.copy())
                return
            
            for i in range(start, n):
                if _has_duplicate(start, i, nums):
                    continue
                nums[i], nums[start] = nums[start], nums[i]
                _permute(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        _permute(0)
        return result

