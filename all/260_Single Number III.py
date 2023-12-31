# 260. Single Number III

# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num_count = collections.Counter(nums)
        result = []
        for num, count in dict(num_count).items():
            if count != 2:
                result.append(num)
        return result