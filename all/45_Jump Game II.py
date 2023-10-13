# 45. Jump Game II

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        step = [0] * n
        reached = 0
        for i in range(n):
            if i + nums[i] <= reached:
                continue
            if i + nums[i] >= n - 1:
                return step[i] + 1
            for j in range(reached + 1, i + nums[i] + 1):
                step[j] = min(step[j], step[i] + 1) if step[j] else step[i] + 1
            reached = i + nums[i]
        return step[-1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        cur = 0
        while cur < n - 1:
            result += 1
            pre = cur
            for i in range(pre + 1):
                cur = max(cur, i + nums[i])
        return result