# 137. Single Number II

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0  # The bits that have appeared odd and even times
        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)
        return ones