# 73. Set Matrix Zeroes


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [], []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0

        return matrix