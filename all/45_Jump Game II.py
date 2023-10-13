# 45. Jump Game II

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        step = [0] * n
        reached = 0
        for i in range(n):
            if nums[i] + i <= reached:
                continue
            if nums[i] + i >= n - 1:
                return step[i] + 1
            for j in range(reached + 1, nums[i] + i + 1):
                step[j] = step[i] + 1
            reached = nums[i] + i
        return step[-1]