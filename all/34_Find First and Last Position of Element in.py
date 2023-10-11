# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def _firstGreaterEqual(target):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return right

        left = _firstGreaterEqual(target)
        if left < 0 or left >= n or nums[left] != target:
            return [-1, -1]

        return [left, _firstGreaterEqual(target + 1) - 1]
