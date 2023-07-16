# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


a = Solution()
print(a.findPeakElement([1, 2, 3, 1]))