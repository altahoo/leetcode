# 34. Find First and Last Position of Element in Sorted Array

class Solution:  # TLM
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        result = [-1, -1]

        # search the first target 
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        # nums is [] or no target found
        if right < 0 or nums[right] != target:
            return result
        
        result[0] = right

        # search the last target
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        result[1] = right
        return result


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
        
        start = _firstGreaterEqual(target)
        if start < 0 or start >= n or nums[start] != target:
            return [-1, -1]
        return [start, _firstGreaterEqual(target + 1) - 1]