# 96. Unique Binary Search Trees

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            if start < 1 or end > n or start >= end:
                return 1
            
            count = 0
            for i in range(start, end + 1):
                count += (helper(start, i - 1) * helper(i + 1, end))
            memo[(start, end)] = count
            return count
        
        return helper(1, n)