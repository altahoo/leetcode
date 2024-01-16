# 304. Range Sum Query 2D - Immutable

# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.left_top_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.left_top_sum[i + 1][j + 1] = matrix[i][j] + self.left_top_sum[i][j + 1] + self.left_top_sum[i + 1][j] - self.left_top_sum[i][j]
   

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.left_top_sum[row2+1][col2+1] - self.left_top_sum[row1][col2+1] - self.left_top_sum[row2+1][col1] + self.left_top_sum[row1][col1]