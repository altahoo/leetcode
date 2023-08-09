# 54. Spiral Matrix


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        dir_i, x, y = 0, 0, 0
        result = []
        for i in range(m * n):
            result.append(matrix[x][y])
            matrix[x][y] = '#'
            if (dir_i == 0 and y == n - 1) or (dir_i == 1 and x == m - 1) or (dir_i == 2 and y == 0) or matrix[x + dirs[dir_i][0]][y + dirs[dir_i][1]] == '#':
                dir_i = (dir_i + 1) % 4
            x += dirs[dir_i][0]
            y += dirs[dir_i][1]
        return result