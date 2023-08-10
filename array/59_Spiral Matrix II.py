# 59. Spiral Matrix II

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        num = 1
        x, y, dir_i = 0, 0, 0

        for i in range(n * n):
            result[x][y] = num
            print(result)
            num += 1
            if (dir_i == 0 and y == n - 1) or (dir_i == 1 and x == n - 1) or (dir_i == 2 and y == 0) or (result[x+dirs[dir_i][0]][y+dirs[dir_i][1]] != 0):
                dir_i = (dir_i + 1) % 4
            x += dirs[dir_i][0]
            y += dirs[dir_i][1]
        return result
