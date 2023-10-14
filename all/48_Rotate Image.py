# 48. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for col in range(n):
            top, bottom = 0, n - 1
            while top < bottom:
                matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
                top += 1
                bottom -= 1
        
        for row in range(n):
            for col in range(row + 1):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]