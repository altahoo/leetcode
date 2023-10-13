# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            min_val = min(height[left], height[right])
            if height[left] == min_val:
                left += 1
                while left < right and height[left] < min_val:
                    result += min_val - height[left]
                    left += 1
            else:
                right -= 1
                while right > left and height[right] < min_val:
                    result += min_val - height[right]
                    right -= 1
        return result