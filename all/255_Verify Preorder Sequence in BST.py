# 255. Verify Preorder Sequence in Binary Search Tree

# Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:

        min_limit = -float('inf')
        stack = []
        
        for num in preorder:
            while stack and stack[-1] < num:
                min_limit = stack.pop()
                
            if num <= min_limit:
                return False
            
            stack.append(num)
        
        return True