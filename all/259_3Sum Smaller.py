# 259. 3Sum Smaller

# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n - 2):
            left, right = i + 1, n - 1
            cur_target = target - nums[i]
            while left < right:
                if nums[left] + nums[right] < cur_target:
                    # IMPORTANT
                    # TRICKY PART HERE
                    # IF THREESUM < TARGET, THEN BECAUSE THEE ARRAY IS SORTED
                    # ALL NUMBERS IN BETWEEN WILL ALSO BE LESS OR EQUAL TO K
                    # AND THEREFORE BE VALID ANSWERS
                    result += right - left
                    left += 1
                else:
                    right -= 1
        return result