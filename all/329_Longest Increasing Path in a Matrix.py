# 329. Longest Increasing Path in a Matrix

# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]
        result = 0

        def dfs(i, j):
            if cache[i][j]:
                return cache[i][j]
            
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i, next_j = i + x, j + y
                if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j] > matrix[i][j]:
                    cache[i][j] = max(cache[i][j], dfs(next_i, next_j))
            cache[i][j] += 1
            return cache[i][j]

        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result
        