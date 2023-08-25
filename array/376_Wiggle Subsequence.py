# 376. Wiggle Subsequence

# A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
# A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

# Given an integer array nums, return the length of the longest wiggle subsequence of nums.

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        positive, negative = [1] * n, [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    positive[i] = max(positive[i], negative[j] + 1)
                elif nums[i] < nums[j]:
                    negative[i] = max(negative[i], positive[j] + 1)
        return max(positive[-1], negative[-1])


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        positive, negative = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                positive = negative + 1
            elif nums[i] < nums[i - 1]:
                negative = positive + 1
        return min(n, max(positive, negative))