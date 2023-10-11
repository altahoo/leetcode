# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if mid > 0 and nums[mid - 1] < target < nums[mid]:
                return mid
            if mid < len(nums) and nums[mid] < target < nums[mid + 1]:
                return mid + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1