# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # A height-balanced binary tree is defined as a binary tree in which the height of the left and the right subtree of any node differ by not more than 1
        def _depth(node):
            if not node:
                return 0
            return max(_depth(node.left), _depth(node.right)) + 1
        
        if not root:
            return True
        if abs(_depth(root.left) - _depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False