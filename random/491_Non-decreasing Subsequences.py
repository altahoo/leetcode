# 491. Non-decreasing Subsequences

# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        return list(set(tuple(i) for i in self.generator(0, [], nums)))
    
    def generator(self, start, path, nums):
        if len(path) > 1:
            yield path
        for i in range(start, len(nums)):
            if not path or nums[i] >= path[-1]:
                yield from self.generator(i + 1, path + [nums[i]], nums)