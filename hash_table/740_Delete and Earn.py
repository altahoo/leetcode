# 740. Delete and Earn

# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        sums = [0] * 10001
        for num in nums:
            sums[num] += num
        for i in range(2, len(sums)):
            sums[i] = max(sums[i - 1], sums[i - 2] + sums[i])
        return sums[-1]