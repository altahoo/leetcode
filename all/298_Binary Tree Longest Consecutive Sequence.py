# 298. Binary Tree Longest Consecutive Sequence

# Given the root of a binary tree, return the length of the longest consecutive sequence path.

# A consecutive sequence path is a path where the values increase by one along the path.

# Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        self.max_length = 0
        def dfs(node, parent, length):
            if not node:
                return
            
            if parent and node.val == parent.val + 1:
                length += 1
            else:
                length = 1
            self.max_length = max(self.max_length, length)

            dfs(node.left, node, length)
            dfs(node.right, node, length)
        
        dfs(root, None, 0)
        return self.max_length