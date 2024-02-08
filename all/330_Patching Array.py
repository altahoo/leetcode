# 330. Patching Array

# Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

# Return the minimum number of patches required.

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, i = 0, 0
        miss = 1
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches