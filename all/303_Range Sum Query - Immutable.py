# 303. Range Sum Query - Immutable

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_till_here = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                self.sum_till_here[0] = num
            else:
                self.sum_till_here[i] = num + self.sum_till_here[i - 1]
        

    def sumRange(self, left: int, right: int) -> int: 
        start = self.sum_till_here[left - 1] if left > 0 else 0
        return self.sum_till_here[right] - start
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)