# 130. Surrounded Regions

# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        queue = collections.deque()

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    board[i][j] = '*'
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()
            for x, y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                next_i = i + x
                next_j = j + y
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == 'O':
                    board[next_i][next_j] = '*'
                    queue.append((next_i, next_j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'