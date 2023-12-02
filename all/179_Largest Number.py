# 179. Largest Number

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

class LargeNumKey(str):
    def __lt__(a, b):
        return a + b > b + a


class Solution:    
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=LargeNumKey)
        result = ''.join(nums)
        return result if result[0] != '0' else '0'
