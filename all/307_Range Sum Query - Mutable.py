# 307. Range Sum Query - Mutable

# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


# TLE
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum_till_here = []
        for num in nums:
            if not self.sum_till_here:
                self.sum_till_here.append(num)
            else:
                self.sum_till_here.append(num + self.sum_till_here[-1])
    
    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index] 
        self.nums[index] = val
        for i in range(index, len(self.nums)):
            self.sum_till_here[i] += delta  

    def sumRange(self, left: int, right: int) -> int:
        start = self.sum_till_here[left - 1] if left > 0 else 0
        return self.sum_till_here[right] - start


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = sum(nums)
    
    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index] 
        self.sum += delta
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1]) if right-left < len(self.nums)//2 else self.sum - sum(self.nums[:left]) - sum(self.nums[right+1:])
        
