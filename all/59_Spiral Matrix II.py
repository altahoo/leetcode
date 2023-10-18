# 59. Spiral Matrix II

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = 0, 0
        num = 1
        cur_dir = 0
        while num <= n * n:
            result[i][j] = num
            next_i = i + dirs[cur_dir][0]
            next_j = j + dirs[cur_dir][1]

            if not (0 <= next_i < n and 0 <= next_j < n) or result[next_i][next_j] > 0:
                cur_dir = (cur_dir + 1) % len(dirs)
            
            i = i + dirs[cur_dir][0]
            j = j + dirs[cur_dir][1]
            num += 1
        return result
