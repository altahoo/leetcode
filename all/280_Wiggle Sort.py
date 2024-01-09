# 280. Wiggle Sort

# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# You may assume the input array always has a valid answer.


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]