# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i < n and nums[i] != 0:
            i += 1
        zero = i

        for j in range(i + 1, n):
            if nums[j] and j > zero:
                nums[j], nums[zero] = nums[zero], nums[j]
                zero += 1