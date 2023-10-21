# 64. Minimum Path Sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        table = [[0] * n for _ in range(m)]
        table[0][0] = grid[0][0]

        for i in range(1, m):
            table[i][0] = grid[i][0] + table[i - 1][0]
        
        for j in range(1, n):
            table[0][j] = grid[0][j] + table[0][j - 1]
        
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = grid[i][j] + min(table[i - 1][j], table[i][j - 1])
        
        return table[m - 1][n - 1]