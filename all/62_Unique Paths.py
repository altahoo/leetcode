# 62. Unique Paths

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0] * n for _ in range(m)]
        for i in range(m):
            table[i][0] = 1
        for j in range(n):
            table[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i][j - 1] + table[i - 1][j]
        
        return table[m - 1][n - 1]