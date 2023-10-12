# 37. Sudoku Solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board) # n = 9
        
        def _is_valid(i, j, ch):
            for k in range(9):
                if board[i][k] == ch or board[k][j] == ch or board[3 * (i // 3) + k // 3][3 * (j // 3) + k % 3] == ch:
                    return False
            return True
        
        def _solve(i, j):
            if i == n:
                return True
            if j == n:
                return _solve(i + 1, 0)

            if board[i][j] != '.':
                return _solve(i, j + 1)
            
            for k in range(1, 10):
                if _is_valid(i, j, str(k)):
                    board[i][j] = str(k)
                    if _solve(i, j + 1):
                        return True
                    board[i][j] = '.'        
            return False

        return _solve(0, 0)