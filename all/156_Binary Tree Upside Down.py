# 156. Binary Tree Upside Down

# Given the root of a binary tree, turn the tree upside down and return the new root.

# You can turn a binary tree upside down with the following steps:

# The original left child becomes the new root.
# The original root becomes the new right child.
# The original right child becomes the new left child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        
        left, right = root.left, root.right
        new_root = self.upsideDownBinaryTree(left)
        left.left = right
        left.right = root
        root.left = None
        root.right = None

        return new_root
