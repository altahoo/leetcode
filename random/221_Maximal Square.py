# 221. Maximal Square

# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # (i, j) is the bottom right corner of the maximal square
        # dp[i][j] is the side length of the maximal square
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0) and matrix[i][j] == '1':
                    dp[i][j] = 1
                elif matrix[i][j] == '1':
                    dp[i][j] = min([dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]]) + 1
                max_side = max(max_side, dp[i][j])

        return max_side * max_side
