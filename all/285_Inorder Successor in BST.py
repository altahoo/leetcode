# 285. Inorder Successor in BST

# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

# The successor of a node p is the node with the smallest key greater than p.val.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        sucessor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                sucessor = root
                root = root.left
        return sucessor