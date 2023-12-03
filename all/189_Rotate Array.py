# 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative

# 根据热心网友 waruzhi 的留言，这道题其实还有种类似翻转字符的方法，思路是先把前 n-k 个数字翻转一下，再把后k个数字翻转一下，最后再把整个数组翻转一下：

# 1 2 3 4 5 6 7 
# 4 3 2 1 5 6 7 
# 4 3 2 1 7 6 5
# 5 6 7 1 2 3 4

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Solution 1: extra space O(n)
        """
        def _reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        n = len(nums)
        k %= n
        _reverse(0, n - k - 1) # Reverse the first n - k
        _reverse(n - k, n - 1) # Reverse the last k
        _reverse(0, n - 1) # Reverse the entire list
        
        return nums