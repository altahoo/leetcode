# 264. Ugly Number II

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        while len(nums) < n:
            n2, n3, n5 = nums[i2] * 2, nums[i3] * 3, nums[i5] * 5
            num = min(n2, n3, n5)
            if num == n2:
                i2 += 1
            elif num == n3:
                i3 += 1
            else:
                i5 += 1
            if num != nums[-1]:
                nums.append(num)
        return nums[-1]
