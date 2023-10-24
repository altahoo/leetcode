# 74. Search a 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        num = m * n
        left, right = 1, m * n
        if num == 1:
            return target == matrix[0][0]
        while left <= right:
            mid = left + (right - left) // 2
            row = (mid - 1) // n
            col = mid % n - 1
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False