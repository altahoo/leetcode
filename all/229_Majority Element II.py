# 229. Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        num_count = collections.Counter(nums)
        for num, count in num_count.items():
            if count > len(nums) / 3:
                result.append(num)
        return result