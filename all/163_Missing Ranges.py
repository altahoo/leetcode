# 163. Missing Ranges

# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        result = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                result.append([nums[i - 1] + 1, nums[i] - 1])
        if nums[0] != lower:
            result = [[lower, nums[0] - 1]] + result
        if nums[-1] != upper:
            result += [[nums[-1] + 1, upper]]
        return result
