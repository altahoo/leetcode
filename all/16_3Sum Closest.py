# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        total = 0
        result = 0

        n = len(nums)
        for i in range(n - 2):
            cur = nums[i]
            left, right = i + 1, n - 1
            while left < right:
                total = cur + nums[left] + nums[right]
                if total == target:
                    return target
                if total > target:
                    diff = total - target
                    right -= 1
                else:
                    diff = target - total
                    left += 1
                if diff < min_diff:
                    result = total
                    min_diff = diff

        return result
