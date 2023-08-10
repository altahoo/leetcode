# 289. Game of Life

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                board[i][j] = [board[i][j]]

        def _get_neighbors(i, j):
            live, dead = 0, 0
            for dir_x, dir_y in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                x = i + dir_x
                y = j + dir_y
                if 0 <= x < m and 0 <= y < n:
                    if board[x][y][0] == 0:
                        dead += 1
                    else:
                        live += 1
            return live, dead
        
        for i in range(m):
            for j in range(n):
                live, dead = _get_neighbors(i, j)
                if board[i][j][0] == 1:
                    if live < 2 or live > 3:
                        board[i][j].append(0)
                    else:
                        board[i][j].append(1)
                else:
                    if live == 3:
                        board[i][j].append(1)
                    else:
                        board[i][j].append(0)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j][1]


sol = Solution()
sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])