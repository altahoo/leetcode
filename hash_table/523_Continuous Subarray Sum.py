# 523. Continuous Subarray Sum

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

# a % c == b % c
# a = mc + d;
# b = nc + d;
# a - b = mc + d - (nc + d) = (m - n) * c

# so (a - b) % c == 0


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        remainders = set()
        pre = 0
        for i in range(len(nums)):
            total += nums[i]
            remainder = total if k == 0 else total % k
            if remainder in remainders:
                return True
            remainders.add(pre)  # Add the value of nums[i - 1] so the subarray's length is at least two 
            pre = remainder
        return False