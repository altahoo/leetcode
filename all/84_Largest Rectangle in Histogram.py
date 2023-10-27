# 84. Largest Rectangle in Histogram

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights + [0]):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] if stack else i
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area