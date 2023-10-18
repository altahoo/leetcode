# 54. Spiral Matrix

# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        result = []
        i, j = 0, 0
        while i < m and j < n and len(result) < m * n:
            result.append(matrix[i][j])
            visited.add((i, j))
            next_x = i + dirs[cur_dir][0]
            next_y = j + dirs[cur_dir][1]

            if not (0 <= next_x < m and 0 <= next_y < n) or (next_x, next_y) in visited:
                cur_dir = (cur_dir + 1) % len(dirs)
            i = i + dirs[cur_dir][0]
            j = j + dirs[cur_dir][1]
        
        return result