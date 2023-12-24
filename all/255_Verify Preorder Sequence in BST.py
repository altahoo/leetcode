# 255. Verify Preorder Sequence in Binary Search Tree

# Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:

        min_val = -float('inf') # the value of the root
        stack = [] # store the left branch

        for num in preorder:
            while stack and stack[-1] < num:
                min_val = stack.pop()
            if num <= min_val:
                return False
            stack.append(num)
        return True