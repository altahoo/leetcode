# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = 0

        for i, num in enumerate(nums):
            if i > reached:
                return False
            reached = max(reached, i + num)
            if reached >= len(nums) - 1:
                return True
