# 52. N-Queens II

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0

        def _solve(row, excluded):
            if row == n:
                self.result += 1
                return

            for col in range(n):
                if (row, col) in excluded:
                    continue
                
                excludes = set()
                r = row
                while r < n:
                    r += 1
                    excludes.add((r, col))
                
                r, c = row, col
                while c < n:
                    c += 1
                    r += 1
                    excludes.add((r, c))

                r, c = row, col
                while c > 0:
                    c -= 1
                    r += 1
                    excludes.add((r, c))
            
                _solve(row + 1, excluded | excludes)
        
        _solve(0, set())
        return self.result