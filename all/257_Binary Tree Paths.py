# 257. Binary Tree Paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def helper(node, sol):
            if not node:
                return

            sol += str(node.val)
            if not node.left and not node.right:
                result.append(sol)
            else:
                sol += '->'
                helper(node.left, sol)
                helper(node.right, sol)
        
        result = []
        helper(root, '')
        return result