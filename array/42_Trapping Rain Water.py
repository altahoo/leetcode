# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        level = 0
        result = 0
        while left < right:
            if height[left] < height[right]:
                lower = height[left]
                left += 1
            else:
                lower = height[right]
                right -= 1
            level = max(level, lower)
            result += level - lower
        return result