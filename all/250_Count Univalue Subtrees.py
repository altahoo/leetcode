# 250. Count Univalue Subtrees

# Given the root of a binary tree, return the number of uni-value subtrees.

# A uni-value subtree means all nodes of the subtree have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                
                self.count += 1
                return True
            
            return False
        
        dfs(root)
        return self.count
