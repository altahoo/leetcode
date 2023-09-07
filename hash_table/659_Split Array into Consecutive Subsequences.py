# 659. Split Array into Consecutive Subsequences

# You are given an integer array nums that is sorted in non-decreasing order.

# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.

# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        num_count = collections.Counter(nums)
        can_append = collections.defaultdict(int)
        for num in nums:
            if not num_count[num]:
                continue
            num_count[num] -= 1

            if can_append[num - 1] > 0:
                can_append[num - 1] -= 1
                can_append[num] += 1
            elif num_count[num + 1] and num_count[num + 2]:
                num_count[num + 1] -= 1
                num_count[num + 2] -= 1
                can_append[num + 2] += 1
            else:
                return False
            
        return True

        