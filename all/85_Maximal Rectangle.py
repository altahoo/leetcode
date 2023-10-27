# 85. Maximal Rectangle

# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + int(matrix[i][j]) if int(matrix[i][j]) == 1 else 0
            result = max(result, self.largestRectangleArea(heights))
        return result
    
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area