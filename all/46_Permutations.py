# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def _permute(start):
            if start == n - 1:
                result.append(nums.copy())
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                _permute(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        _permute(0)
        return result