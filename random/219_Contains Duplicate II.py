# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_idx = {}
        for idx, num in enumerate(nums):
            if num in num_idx and idx - num_idx[num] <= k:
                return True
            num_idx[num] = idx
        return False