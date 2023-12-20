# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        x, y = len(matrix) - 1, 0
        while True:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
            if x < 0 or y >= len(matrix[0]):
                return False
        return False