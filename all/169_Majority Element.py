# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                result = num
                continue
            if result == num:
                cnt += 1
            else:
                cnt -= 1
        return result