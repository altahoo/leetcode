# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = n
        for i, num in enumerate(nums):
            if num == 0 and zero == n:
                zero = i
            if num and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1